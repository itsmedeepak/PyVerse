import PyPDF2

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"Merged PDFs saved as {output}")

def split_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_file = f"{pdf_file}_page_{page_num+1}.pdf"
        with open(output_file, "wb") as f:
            pdf_writer.write(f)
        print(f"Page {page_num+1} saved as {output_file}")

def extract_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    print("Extracted Text:\n", text)
    return text

def main():
    print("PDF Manipulator")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Extract Text")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        files = input("Enter PDF files separated by comma: ").split(",")
        output = input("Enter output file name: ")
        merge_pdfs(files, output)
    elif choice == "2":
        file = input("Enter PDF file to split: ")
        split_pdf(file)
    elif choice == "3":
        file = input("Enter PDF file to extract text from: ")
        extract_text(file)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
