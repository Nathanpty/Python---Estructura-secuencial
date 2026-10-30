palabra = str(input("Escribe 'Hola' o 'Salir':  "))
while palabra != "salir":
    if palabra == "Hola":
        print("¡Hola, mucho gusto!")
    elif palabra == "Salir":
        print("¡Hasta luego!")
    else:
        print("Opción no válida")
    palabra = str(input("Escribe 'Hola' o 'Salir':"))
