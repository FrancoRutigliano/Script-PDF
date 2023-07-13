import PyPDF2
import os

Ruta_archivo = './Archivos'  # Ruta de la carpeta que contiene los archivos PDF a combinar
Ruta_salida = 'combinados.pdf'  # Ruta y nombre de archivo para el PDF combinado

#Creando una instancia de la clase PyPDF2 del metodo PDFMerger()
merger = PyPDF2.PdfMerger()

for file in os.listdir(Ruta_archivo):
    if file.endswith(".pdf"):
        file_path = os.path.join(Ruta_archivo, file)
        merger.append(file_path)

merger.write(Ruta_salida)
merger.close()

print("Archivos PDF combinados con éxito.")


