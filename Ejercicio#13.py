palabra = str(input("Ingrese una palabra: "))
vocales = 0
for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales += 1
print(f"El número de vocales en la palabra es: {vocales}")