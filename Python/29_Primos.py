print("Inicio")
i = 0

def es_primo(num):
                #Empieza a iterar siempre desde el dos hasta num(i)
    for n in range(2, num):
        if num % n == 0:
            return False
    print(f"Es primo: {num}")
while True:
    i = i + 1
    es_primo(i)


print("Fin")