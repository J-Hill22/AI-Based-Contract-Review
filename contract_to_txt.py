import docx2txt
from docx import Document
from PyPDF2 import PdfReader

# Function to process and clean the content of a DOCX file
def _clean_docx(docx_path):
    # Extract text from the DOCX file
    raw_text = docx2txt.process(docx_path)
    
    # Remove leading and trailing white spaces from each line
    lines = raw_text.strip().split('\n')
    cleaned_lines = [line.strip() for line in lines]
    
    # Remove empty lines
    cleaned_lines = [line for line in cleaned_lines if line]
    
    # Join the lines back
    cleaned_text = '\n'.join(cleaned_lines)

    with open('contract_to_txt.txt', 'w', encoding="utf-8") as file:
        file.write(cleaned_text)
    

# Function to process and clean the content of a PDF file
def _clean_pdf(pdf_path):
    pdf_file_obj = open(pdf_path, 'rb')

    pdf_reader = PdfReader(pdf_file_obj)

    page_count = len(pdf_reader.pages)

    page_obj = pdf_reader.pages[page_count - 1]

    pdf_text = ''

    for i in range(page_count - 1):
        page_obj = pdf_reader.pages[i]
        pdf_text += (page_obj.extract_text())

    with open('contract_to_txt.txt', 'w', encoding="utf-8") as file:
        file.write(pdf_text)

# Function to convert a txt file to docx file
def txt_to_docx(txt_filepath, cleaned_docx_filepath):
    # Initialize a Document
    doc = Document()
    
    # Open and read the txt file
    with open(txt_filepath, 'r', encoding = "utf8") as txt_file:
        # Loop over each line in the txt file
        for line in txt_file:
            # Add a paragraph for each line in txt to docx
            doc.add_paragraph(line.strip())
            
    # Save the Document
    doc.save(cleaned_docx_filepath)

def convert_to_txt(contract_in):
    dot_pdf = '.pdf'
    dot_docx = '.docx'
    if contract_in.endswith(dot_pdf):
        _clean_pdf(contract_in)
    elif contract_in.endswith(dot_docx):
        _clean_docx(contract_in)
    else:
        return ('Error: unexpected file type')


