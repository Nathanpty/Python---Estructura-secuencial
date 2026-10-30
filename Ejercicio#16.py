suma = 0 
cantidad = 0 
nota = float(input("Ingresa tus notas,si quiere dejar de contar notas, ingresa -1 : ")) 
while nota != -1: 
    suma += nota 
    cantidad += 1 
    nota = float(input("Ingresa tus notas,si quiere dejar de contar notas, ingresa -1 :")) 
if cantidad > 0: 
    print("Promedio:", suma / cantidad) 
else: 
    print("No ingresaste notas") 