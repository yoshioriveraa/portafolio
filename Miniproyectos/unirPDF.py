import PyPDF2

def merge_pdfs(input_files, output_file):
    pdf_merger = PyPDF2.PdfFileMerger()

    for file in input_files:
        with open(file, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_file, 'wb') as merged_pdf:
        pdf_merger.write(merged_pdf)

# Rutas de los archivos PDF de entrada y archivo PDF de salida
input_files = ['TRABAJO01.pdf', 'TRABAJO01-2.pdf']
output_file = 'TRABAJO01-FINAL.pdf'

# Llamada a la función para unir los archivos
merge_pdfs(input_files, output_file)