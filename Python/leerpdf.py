import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog

def extract_text_from_pdf(pdf_path):
    try:
        # Abre el archivo PDF
        document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error al abrir el archivo PDF: {e}")
        return ""
    
    # Extrae el texto de cada página
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    
    return text

def select_file():
    # Crea una ventana oculta
    root = tk.Tk()
    root.withdraw()
    
    # Abre un diálogo para seleccionar el archivo
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo PDF",
        filetypes=[("Archivos PDF", "*.pdf"), ("Todos los archivos", "*.*")]
    )
    
    return file_path

def main():
    # Permite al usuario seleccionar el archivo
    pdf_path = select_file()
    
    if not pdf_path:
        print("No se seleccionó ningún archivo.")
        return
    
    # Extrae el texto
    text = extract_text_from_pdf(pdf_path)
    
    if text:
        # Muestra el texto extraído
        print("Texto extraído del PDF:")
        print(text)
        
        # Opcional: guardar el texto en un archivo
        with open("extracted_text.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)
    else:
        print("No se pudo extraer texto del archivo PDF.")

if __name__ == "__main__":
    main()
