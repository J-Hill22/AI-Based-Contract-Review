import docx2txt
from docx import Document

# Main Program
def _clean_docx(docx_path):
    # Convert input docx file to a txt
    docx_to_txt = process_and_clean_docx(docx_path)

    # Creates temporary txt file to hold the text scanned from original input file
    txt_name = 'docx_to_text.txt'

    # Creates temporary docx file to hold text for txt->docx file
    docx_name = 'txt_back_to_docx.docx'

    # Writes the docx to a txt file
    with open(txt_name, 'w', encoding="utf-8") as file:
        file.write(docx_to_txt)

    # Converts the txt file back to docx so it can be used with annotate_contract
    txt_to_docx(txt_name, docx_name)
    return docx_name

# Function to process and clean the content of a DOCX file
def process_and_clean_docx(docx_file_path):
    # Extract text from the DOCX file
    raw_text = docx2txt.process(docx_file_path)
    
    # Remove leading and trailing white spaces from each line
    lines = raw_text.strip().split('\n')
    cleaned_lines = [line.strip() for line in lines]
    
    # Remove empty lines
    cleaned_lines = [line for line in cleaned_lines if line]
    
    # Join the lines back
    cleaned_text = '\n'.join(cleaned_lines)
    
    # Returns cleaned text from DOCX file as a string
    return cleaned_text

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