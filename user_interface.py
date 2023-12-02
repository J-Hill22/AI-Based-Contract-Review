import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from flag_FAR_clauses import annotate_contract
from tkinter import filedialog
from contract_to_txt import convert_to_txt, txt_to_docx
from flag_problem_language import _flag_problem_language
from extract_company_details import extract_company_details
from docx import Document
import os
import subprocess
from datetime import datetime

# Read in relevant excel matrices
print("Reading FAR Clause Matrix")
FAR_clause_matrix = 'problem_language_matrices\\2023-03-20_FAR Matrix.xls'
print("Reading AU's Contract Ts&Cs Matrix")
tnc_matrix = 'problem_language_matrices\Contract Ts&Cs Matrix.xlsm'
contract_in = ''
contract_out = ''

file_to_item_id = {}

def update_document_list(file_path, status):
    file_name = os.path.basename(file_path)
    last_modified = os.path.getmtime(file_path)
    last_modified_date = datetime.fromtimestamp(last_modified).strftime("%m/%d/%Y %I:%M %p")
    
    # If this file is already in the list, remove the old entry
    if file_path in file_to_item_id:
        document_list.delete(file_to_item_id[file_path])
    
    # Insert the new entry and update the dictionary
    item_id = document_list.insert("", "end", values=(file_name, last_modified_date, status))
    file_to_item_id[file_path] = item_id

def upload_contract():
   global contract_in  # Declare as global
   contract_in = filedialog.askopenfilename(filetypes=[('Word Documents', '*.docx'), ("PDF Files", "*.pdf")])
   if contract_in:
       update_document_list(contract_in,"Not Scanned")

def scan_contract():
   global contract_out  # Make sure contract_out has been set
   if contract_in and contract_out:
       print('Scanning contract')
       convert_to_txt(contract_in)
       _flag_problem_language(tnc_matrix)
       back_to_docx = 'flagged_contract_to_txt.txt'
       file_to_highlight = 'flagged_contract_to_docx.docx'
       txt_to_docx(back_to_docx, file_to_highlight)
       annotate_contract(FAR_clause_matrix, file_to_highlight, contract_out)
       
        
       # Extract company details and update the company_details_box
       with open('contract_to_txt.txt', 'r',encoding="utf-8") as file:  # Make sure to open your contract file
           contract_text = file.read()
       company_details = extract_company_details(contract_text)
       company_details_str = "\n".join(f"{key}: {value}" for key, value in company_details.items())
       company_details_box.config(state=tk.NORMAL)  # Enable text box for editing
       company_details_box.delete("1.0", tk.END)
       company_details_box.insert("1.0", company_details_str)
       company_details_box.config(state=tk.DISABLED)  # Disable editing after inserting text
       
       print('Finished scanning')
       print(f'Scanned contract saved to: {os.path.basename(contract_out)}')

       # Update the status in the document list
       update_document_list(contract_in, "Scanned")
       update_document_list(contract_out, "Ready To View")
   else:
       print("Error: File paths not set")

def export_contract():
    global contract_out  # Declare as global
    contract_out = filedialog.asksaveasfilename(filetypes=[('Word Documents', '*.docx'), ("PDF Files", "*.pdf")])
    if contract_out:
        if not os.path.exists(contract_out):
            open(contract_out, 'a').close() # Adds placeholder file for GUI readability if not choosing existing file
            
        update_document_list(contract_out, "File Path Saved")

root = tk.Tk()
root.title("Contract Scanner")
root.geometry("800x600")


root.configure(bg="#CCE5FF")


main_frame = tk.Frame(root, bg="#CCE5FF")
main_frame.pack(pady=20)


search_documents = ttk.Label(main_frame, text="Search Documents", font=("Alien League", 12))
search_documents.grid(row=0, column=0, padx=10, pady=10)


search_entry = ttk.Entry(main_frame, font=("Alien League", 12))
search_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=50)
search_entry.insert(0, "TODO: Search Uploaded Documents")
search_entry.config(foreground="grey")


def search_entry_click(event):
   if search_entry.get() == "Search documents":
       search_entry.delete(0, tk.END)
       search_entry.config(foreground="black")


search_entry.bind("<FocusIn>", search_entry_click)


upload_button = ttk.Button(main_frame, text="Select File", command=lambda: upload_contract(), style="Yellow.TButton")
upload_button.grid(row=1, column=0, padx=10, pady=10, ipadx=30)

export_button = ttk.Button(main_frame, text="Save File As...", command=lambda: export_contract(), style="Grey.TButton")
export_button.grid(row=1, column=1, padx=10, pady=10, ipadx=30)

scan_button = ttk.Button(main_frame, text="Scan", command=lambda: scan_contract(), style="Green.TButton")
scan_button.grid(row=1, column=2, padx=10, pady=10, ipadx=30)

document_list = ttk.Treeview(root, columns=("Contract", "Date", "Status"), show="headings")
document_list.heading("Contract", text="Contract")
document_list.heading("Date", text="Date")
document_list.heading("Status", text="Status")
document_list.pack(padx=20, pady=10)

def open_file(event):
    selected_item = document_list.selection()[0]  # This assumes only one selection is allowed at a time
    file_name = document_list.item(selected_item, 'values')[0]  # Get the file name from the first column
    # Find the full file path from the file name
    file_path = next((path for path, name in file_to_item_id.items() if os.path.basename(path) == file_name), None)
    if file_path and os.path.isfile(file_path):
        os.startfile(file_path)  # Open the file using the default application
        # Alternatively, for more control, use subprocess:
        # subprocess.Popen(['start', file_path], shell=True)

# Bind the double-click event
document_list.bind("<Double-1>", open_file)

company_details_box = tk.Text(root, height=5, width=60)  # Adjust height and width as needed
company_details_box.pack(padx=20, pady=10)
company_details_box.insert("1.0", "Company details will be shown here.")
company_details_box.config(state=tk.DISABLED, foreground="grey")  # Initially set to read-only


document_viewer = tk.Text(root, wrap=tk.WORD, font=("Alien League", 12))
document_viewer.pack(padx=20, pady=10)
document_viewer.insert("1.0", "TODO: Edit document text here")
document_viewer.config(foreground="grey")


def document_viewer_click(event):
   if document_viewer.get("1.0", "end-1c") == "Edit document text here":
       document_viewer.delete("1.0", "end-1c")
       document_viewer.config(foreground="black")


document_viewer.bind("<FocusIn>", document_viewer_click)

root.mainloop()