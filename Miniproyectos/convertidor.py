from pdf2docx import Converter

def pdf_to_word(input_pdf, output_word):
    cv = Converter(input_pdf)
    cv.convert(output_word, start=0, end=None)
    cv.close()

# Ruta del archivo PDF de entrada y archivo Word de salida
input_pdf = 'Grey Yellow Geometry Business Wattpad Book Cover.pdf'
output_word = 'caratula.docx'

# Llamada a la función para convertir el archivo
pdf_to_word(input_pdf, output_word)
