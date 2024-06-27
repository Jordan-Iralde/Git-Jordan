'''
Consigna: Un programa que detecte cuando una palabra es un palindromo
'''

Pld = "deed"
m = -1
flag = 0

i = 0

#char va de uno en uno desde d hasta d
for char in Pld:
    i= i +1
    print(char)
    print("m es igual a", m)
    print()

    #Si char es diferente de pld, se corta. Por ejemplo     d d e(hola) e d(hola) != d e d d(char)
    if char != Pld[m]:
        print("hola")
        flag = 1
        break
        #Si es diferente se termina el recorrido(Despues)y entra al if
        
    m = m - 1
print(Pld + " is: ", end="")
if flag:
    print("Not Palindrome")
else:
    print("Palindrome")
print(flag)