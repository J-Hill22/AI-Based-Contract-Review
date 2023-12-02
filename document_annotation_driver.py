from flag_FAR_clauses import annotate_contract
import tkinter
from tkinter import filedialog
from contract_to_txt import convert_to_txt, txt_to_docx
from flag_problem_language import _flag_problem_language
from docx import Document

tkinter.Tk().withdraw()
# Opens file browser to select Excel spreadsheet containing FAR Clauses
print("Reading FAR Clause Matrix")
FAR_clause_matrix = 'problem_language_matrices\\2023-03-20_FAR Matrix.xls'

# Opens file browser to select Excel spreadsheet containing FAR Clauses
print("Reading AU's Contract Ts&Cs Matrix")
tnc_matrix = 'problem_language_matrices\Contract Ts&Cs Matrix.xlsm'

# Opens file browser to select document you wish to parse and annotate according to selected spreadsheet
print("Select contract you wish to annotate")
contract_in = filedialog.askopenfilename()

# Opens file browser and prompts user to save a file and input name for file
print("Select the directory you wish to save annotated contract to")
save_path = filedialog.asksaveasfilename()

print("Scanning Contract")

# clean docx and annotate it
convert_to_txt(contract_in)
_flag_problem_language(tnc_matrix)
back_to_docx = 'flagged_contract_to_txt.txt'
file_to_highlight = 'flagged_contract_to_docx.docx'
txt_to_docx(back_to_docx, file_to_highlight)

annotate_contract(FAR_clause_matrix, file_to_highlight, save_path)

print("Annotation complete. Output file: " + save_path)