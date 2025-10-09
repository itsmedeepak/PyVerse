import streamlit as st
import json
from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.schema import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

#UI styling
page_bg="""
<style>
[data-testid="stAppViewContainer"], [data-testid="stHeader"], #stSpinner {
background-color : #c3b091;
color : #483c32;
}

[data-testid="stHeading"], [data-testid="stWidgetLabel"], #text_area_1 {
color : #483c32
}

[data-testid="stTextAreaRootElement"] {
background-color : #c3b091
}

#text_area_1 {
background-color : #f1e0d2
}

button[kind="secondary"] {
background-color : #483c32;
color : #f1e0d2;
}
<style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

# 1. Data Loading and Splitting
def load_data():
    with open("remedies.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        docs = []
        for item in data:
            # Each item is a dict with one key-value pair
            for key, value in item.items():
                if value.strip():  # skip empty entries
                    docs.append(Document(page_content=value, metadata={"remedy": key}))

        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
        split_docs = splitter.split_documents(docs)

    return split_docs

# 2. Embedding data using HuggingFaceEmbeddings
def get_embeddings(data):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

# 3. Storing embeddings in InMemoryVectorStore
def store_embeddings(embeddings, splitted_data):
    vector_store = InMemoryVectorStore(embeddings)
    ids = vector_store.add_documents(documents=splitted_data)
    return vector_store

#Formatting docs into text stream
def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

#creating RAG response
@st.cache_resource
def rag_response(query):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

    template = """You are an experienced Homeopathic Doctor who has studied from {context}, with extensive knowledge of every homeopathic medicine, its indications, relationships, and comparative remedies for different ailments.

    Your role:

    1. Use only the provided context to answer any questions. Do not include information from outside sources.
    2. Listen carefully to the user’s symptoms or questions.
    3 If a user describes symptoms or an ailment, analyze them and suggest the most suitable remedy or a shortlist of remedies, explaining the reasoning.

    5 If a user asks about a specific medicine, respond in the structure:

    "Medicine Name" — Illnesses it treats — Can be substituted with (other remedies).

    6. Always provide clear, accurate, and compassionate explanations.
    7. Always sound reassuring, calm, and professional, like a real homeopathic physician.

    Format of your response:

    Greeting — brief and kind.
    Observation or understanding of the user’s concern.
    Dosage instructions (if asked) refer to reach out to human doctor.
    Explanation or comparison of relevant remedies (if applicable).
    Closing line — reassuring.

    Use the following variable for user input:

    Question: {question}

    """

    prompt = ChatPromptTemplate.from_template(template)

    remedy_docs = load_data() # 1. load and split
    remedy_embed = get_embeddings(remedy_docs) # 2. embed
    vector_store = store_embeddings(remedy_embed, remedy_docs) # 3. store
    retriever = vector_store.as_retriever(search_kwargs={"k": 6}) # 4. retrieve

    # 5. create chain
    chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
    )

    # 6. get response
    response = chain.invoke(query)
    st.write(response)


#UI
st.title("Remedy AI")
st.header("Welcome to Remedy AI - A Homoepathic Ailment Chatbot")

query = st.text_area(label="Welcome to Remedy AI! Your go-to guide for understanding homeopathic remedies and medicines. Whether you’re looking for tips on managing common illnesses or exploring natural treatments, Remedy AI helps you make informed choices to take better care of your health.", placeholder=" ", height=300)

st.button(label = "Ask Remedy", on_click=click_button, type="secondary")

if st.session_state.clicked and query:
    if not(query):
        st.write("Oops, you didn't enter your question.")
    rag_response(query)


