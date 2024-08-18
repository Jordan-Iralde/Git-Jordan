import tkinter as tk
from tkinter import font
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Crear la ventana principal
window = tk.Tk()
window.title("Reloj en Vivo")

# Configurar la ventana
window.geometry("400x200")  # Tamaño de la ventana
window.resizable(False, False)  # No permitir redimensionar

# Crear una fuente grande
large_font = font.Font(family="Helvetica", size=48, weight="bold")

# Crear y configurar la etiqueta para la hora
time_label = tk.Label(window, font=large_font)
time_label.pack(expand=True)

# Actualizar la hora por primera vez
update_time()

# Iniciar el bucle principal de la ventana
window.mainloop()
