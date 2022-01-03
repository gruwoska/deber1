# Dado un (1) número, imprimir 0 si es par y 1 si es impar.
try:
    a=int(input("Ingrese un numero entero"))
    if a % 2==0:
        print("El numero es par")
    else:
        print("El numero no es par")
except:
    print("No ha ingresado un numero entero")

   