def menu():
    menuInicio = '''
    *********************
    *   1- Pollo        *
    *   2- Lechuga      *
    *   3- Verdura      *
    *   4- Asado        *
    *   5- Salir        *
    *********************
    '''
    return print(menuInicio)

while True:
    try:
        menu()

        opcion = int(input("Ingrese la opcion que usted desee: "))

        if opcion == 1:
            print("Usted A elegido Pollo")
        elif opcion == 2:
            print("Usted A elegido Lechuga")
        elif opcion == 3:
            print("Usted A elegido Verdura")
        elif opcion == 4:
            print("Usted A elegido Asado")
        elif opcion == 5:
            break
        else:
            print("No eligio nada, opcion para volver al menu_")
        
        volverMenu = int(input("volver al menu?, ingrese 1: "))

        if volverMenu == 1:
            print()
        else:
            print("Saliendo...")
            break
    except ValueError():
        print("Dato no valido")