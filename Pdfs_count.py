import os
import PyPDF2

pdf_directory = r'C:\Users\vivif\Documents\K Kotapadu-20231102T071451Z-001\K Kotapadu'
total_page_count = 0

def count_pages_and_extract_text(pdf_file):
    global total_page_count  # Declare total_page_count as global
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        total_page_count += num_pages
        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return num_pages, text

pdf_files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

for pdf_file in pdf_files:
    num_pages, text = count_pages_and_extract_text(pdf_file)
    print(f"File: {pdf_file}, Pages: {num_pages}, Text: {text}")

print(f"Total Page Count: {total_page_count}")
