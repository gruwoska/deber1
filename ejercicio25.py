# Construya un programa que dado un valor entero N, haga el cálculo de la función factorial utilizando estructuras iterativas.
numero=int(input("Ingrese un numero entero:"))
def factorial(n):
    f=1
    while n>1:
        f*=n
        n-=1
    print(f)
factorial(numero)
