number = int(input("Ingrese un número del 1 - 10:"))
if number >=10:
    print("El número no es válido")
elif number <10 and number >7:
    print("Uff, eso estuvo cerca")
elif number <7 and number >=1:
    print("El número es muy bajo")
elif number <1:
    print("El número es no es válido")
else:
    print("El número está correcto")