# Suma de Recursividad e Iterativa
#hazel yorelly perez hernandez

def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        return suma_recursiva(n // 10) + n % 10

while True:
    print("__________________\n")
    print(":) Ejercios de las sumas recursivas e iterativa :) \n")
    print("__________________\n")
    print("Presione 1 para la suma recursiva, 2 para la suma iterativa o 3 para salir. \n")
    print("1.- La suma Recursiva. \n")
    print("2.- La suma Iterativa. \n")
    print("3.- Salir. \n")

    las_opciones = int(input("Ingrese una opción: "))

    if las_opciones == 1:
        operacion = int(input("Ingrese un número para la respectiva suma recursiva: "))
        print("Suma recursiva:", suma_recursiva(operacion))
    elif las_opciones == 2:
        operacion = int(input("Ingrese un número para la respectiva suma iterativa: "))
        print("Suma iterativa:", suma_iterativa(operacion))
    elif las_opciones == 3:
        print("fin del programa :)")
    else:
        print("error con la opcion :(.")
        break 