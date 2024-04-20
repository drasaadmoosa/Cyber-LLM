import os
import pdfplumber

def convert_pdf_to_txt(pdf_file_path, txt_file_path):
    """Convert a PDF file to a text file using pdfplumber."""
    with pdfplumber.open(pdf_file_path) as pdf:
        with open(txt_file_path, 'w', encoding='utf-8') as text_file:
            for page in pdf.pages:
                text_file.write(page.extract_text())

def process_folder(pdf_folder, txt_folder):
    """Process all PDF files in the specified folder and convert them to text files."""
    if not os.path.exists(txt_folder):
        os.makedirs(txt_folder)
        print(f"Created text file directory at {txt_folder}")

    for file_name in os.listdir(pdf_folder):
        if file_name.lower().endswith('.pdf'):
            pdf_file_path = os.path.join(pdf_folder, file_name)
            txt_file_name = f"{os.path.splitext(file_name)[0]}.txt"
            txt_file_path = os.path.join(txt_folder, txt_file_name)
            convert_pdf_to_txt(pdf_file_path, txt_file_path)
            print(f"Converted {file_name} to TXT.")

# Paths to the folders
pdf_folder = 'files/PDFs'  # Path to the folder containing the PDF files
txt_folder = 'files/TXTs'  # Path to the folder where the TXT files will be saved

process_folder(pdf_folder, txt_folder)
