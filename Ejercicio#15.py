dinero = 1
dias = int(input("Ingrese la cantidad de días que desea ahorrar, solo números: "))
for i in range(dias):
    dinero *= 2

print("En", dias, "días tendrás ahorrado:", dinero, "dólares")