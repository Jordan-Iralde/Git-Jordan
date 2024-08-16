def CodigoMIO():

    print("Inicio")
    resistencias = {}

    while True:
        voltaje = int(input("Ingrese Voltaje: "))
        resistenciasSerie = []
        resistenciasParalelos = []

        CantidadResistencias = int(input("Ingrese la cantidad de resistencias que se encuentran: "))
        for i in range(CantidadResistencias):

            serieParalelo = input("Su resistencia es en serie o paralelo: ")

            if serieParalelo == 'serie':
                resistencia = int(input(f"Resistencia {i+1}: \n"))
                resistenciasSerie.append(resistencia)
                resistencias[i] = resistencia

            elif serieParalelo == 'paralelo':
                resistencia = int(input(f"Resistencia {i+1}: \n"))
                calculoResistenciaparalelo = 1/resistencia
                resistenciasParalelos.append(calculoResistenciaparalelo)
                print("La resistencia total paralelo es", sum(resistenciasParalelos))
            else:
                print("mal ingresado")
                exit()

        if len(resistenciasParalelos) == 1:
            print("Error, para ser paralelo deben haber 2 resistencias minimo")

        RpT = 1/sum(resistenciasParalelos)
        resistenciaTotal = sum(resistenciasSerie) + RpT
        print("Resistencia Total= ", resistenciaTotal)

        IntensidadTotal = voltaje / resistenciaTotal
        print("Intensidad Total= ", IntensidadTotal)
        
        print(resistencias)

    #Calcular Intensidad
    #Calcular Voltaje

    print("Fin")
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Import correcto
import numpy as np

def actualizar_grafico(resistenciasSerie, resistenciasParalelos):
    plt.clf()
    if resistenciasSerie:
        plt.plot([0, 1], [1, 1], color='blue')  # Línea para resistencias en serie
        for i in range(len(resistenciasSerie)):
            plt.text(0.5 + i, 1, f"R{i+1}={resistenciasSerie[i]}", color='blue')

    if resistenciasParalelos:
        plt.plot([0.5, 0.5], [0, 1], color='red')  # Ramas paralelas
        for i in range(len(resistenciasParalelos)):
            plt.text(0.5, 0.5 - i, f"Rp{i+1}={1/resistenciasParalelos[i]}", color='red')

    plt.draw()

def agregar_resistencia():
    tipo = tipo_resistencia.get()
    valor = float(entry_resistencia.get())
    
    if tipo == 'serie':
        resistenciasSerie.append(valor)
    elif tipo == 'paralelo':
        resistenciasParalelos.append(1/valor)
        
    actualizar_grafico(resistenciasSerie, resistenciasParalelos)

resistenciasSerie = []
resistenciasParalelos = []

root = tk.Tk()
root.title("Circuito Resistencia")

frame = tk.Frame(root)
frame.pack()

label_voltaje = tk.Label(frame, text="Voltaje:")
label_voltaje.pack(side="left")
entry_voltaje = tk.Entry(frame)
entry_voltaje.pack(side="left")

label_resistencia = tk.Label(frame, text="Resistencia:")
label_resistencia.pack(side="left")
entry_resistencia = tk.Entry(frame)
entry_resistencia.pack(side="left")

tipo_resistencia = tk.StringVar(value='serie')
radio_serie = tk.Radiobutton(frame, text="Serie", variable=tipo_resistencia, value='serie')
radio_paralelo = tk.Radiobutton(frame, text="Paralelo", variable=tipo_resistencia, value='paralelo')
radio_serie.pack(side="left")
radio_paralelo.pack(side="left")

boton_agregar = tk.Button(frame, text="Agregar Resistencia", command=agregar_resistencia)
boton_agregar.pack(side="left")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)  # Uso correcto de FigureCanvasTkAgg
canvas.get_tk_widget().pack()

root.mainloop()