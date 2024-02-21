# -*- coding: utf-8 -*-
"""
Extract text from PDF files in an input directory and write the raw text into
TXT files in the output directory

@author: K. Nolle
"""

from pypdf import PdfReader
import os

input_dir = "./data/pdfs"
output_dir = "./data/raw-txt"

# Create output directory if missing
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Extract text from PDFs
for pdf_filename in os.listdir(input_dir):
    print(f"Extracting text from {pdf_filename}")
    
    txt_filename = os.path.splitext(pdf_filename)[0] + ".txt"
    txt_path = os.path.join(output_dir, txt_filename)
    
    pdf_path = os.path.join(input_dir, pdf_filename)
    
    reader = PdfReader(pdf_path)
    
    with open(txt_path, 'wb') as output_file:
        for page in reader.pages:
            text = page.extract_text() + "\n"
            output_file.write(text.encode('utf-8', 'replace'))


"""
with open(args.output, 'w', encoding='ascii') as output_file:
    if args.header is not None:
        output_file.write(args.header + "\n")
            
    # Load the TFLite model and allocate tensors.
    interpreter =  tflite.Interpreter(model_path=args.model_name + '.tflite')
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    


"""