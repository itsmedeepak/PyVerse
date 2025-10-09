# REMEDY AI

Remedy AI is a RAG implemented app built to answer queries about ailments and remedies in Homeopathy.

## What is RAG?

RAG stands for Retrieval-Augmented Generation. It’s a technique that combines information retrieval with text generation - allowing a language model to generate responses using external context or data it retrieves at runtime.

In other words, instead of relying only on what it was trained on, the model can fetch relevant information from a knowledge base or documents and use that to produce accurate, context-aware answers.

This project is a knowledge-based assistant that acts as a Homeopathic Expert powered by a large language model.

## Stack

The project is built purely using Python with Langchain and Streamlit. Required Documentation to build this project can be found: [here](https://python.langchain.com/docs/tutorials/rag/) and [here](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)

## Project Structure

```
remedy-ai-rag
│
├── main.py
├── remedies.json
├── requirements.txt
└── .env
│
remedy-ai-scraper
│
├── spiders/
│   └──materia.py
│
│── remedies.json
│
└── README.md
```

## Project Setup

 Get your Langchain API Key from signing up [here](https://www.langchain.com/langchain)
 Get your Google API Key [here](https://aistudio.google.com/app/api-keys)

 Jump to `remedy-ai-rag` folder

  Add YOUR_API_KEY in `remedy-ai-rag/.env`

```.env
LANGSMAITH_API_KEY=your-api-key
LANGSMITH_TRACING=true
GOOGLE_API_KEY=your-google-api-key
```

 Install requirements

```
pip install -r requirements.txt
```

 Run your code

```
streamlit run main.py
```

To run the web scraping script install Scrapy and run the command

```
scrapy crawl boericke -o remedies.json
```
