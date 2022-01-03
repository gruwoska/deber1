# Dado un número, determine si es capicúa.
a=str(input("Ingrese un numero: "))
a=list(a)
b=a[::-1]
if a==b:
    print("Si es un numero capicua")
else:
    print("No es un numero capicua")