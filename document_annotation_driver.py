from annotate_contract import annotate_contract
import tkinter
from tkinter import filedialog
from docx_parser import _clean_docx

# Opens file browser to select Excel spreadsheet containing problematic language
tkinter.Tk().withdraw()
print("Select FAR Matrix from file browser")
xls_in = filedialog.askopenfilename()

# Opens file browser to select document you wish to parse and annotate according to selected spreadsheet
print("Select contract you wish to annotate")
contract_in = filedialog.askopenfilename()

# Opens file browser and prompts user to save a file and input name for file
print("Select the directory you wish to save annotated contract to")
save_path = filedialog.asksaveasfilename()

# clean docx and annotate it
cleaned_docx = _clean_docx(contract_in)

annotate_contract(xls_in, cleaned_docx, save_path)

print("Annotation complete. Output file: " + save_path)