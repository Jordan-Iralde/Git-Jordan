'''
Escribe una función que encuentre el número más pequeño y el más grande en una lista de enteros, 
todo en una sola pasada (es decir, recorriendo la lista una sola vez). El reto aquí es optimizar 
el código para que sea lo más eficiente posible en tiempo y espacio.

Entrada:
lista = [34, -2, 45, 3, 0, -5, 99]

Salida:
El número más pequeño es: -5
El número más grande es: 99
'''

lista = [34, -2, 45, 3, 0, -5, 99]
def EncontrarMaxMin(lista):
    minimoDeLista, maximoDeLista = 0, 0
    for i in lista:
        if i <= 0 and minimoDeLista > i:
            minimoDeLista = i
        if i > 0 and maximoDeLista < i:
            maximoDeLista = i
    return minimoDeLista, maximoDeLista
valores = EncontrarMaxMin(lista)
print(f"El número más pequeño es: {valores[0]}")
print(f"El número más grande es: {valores[1]}")

'''
De esta manera se pueden encontrar los valores mayores y menores a pesar de tener numeros negativos u otros.

def encontrar_max_min(lista):
    # Inicializa mínimo y máximo con el primer valor de la lista
    minimo_de_lista = maximo_de_lista = lista[0]
    
    for i in lista:
        if i < minimo_de_lista:
            minimo_de_lista = i
        if i > maximo_de_lista:
            maximo_de_lista = i
            
    return minimo_de_lista, maximo_de_lista
'''