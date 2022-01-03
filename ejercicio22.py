# Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
# dicho número.
a=True
while a==True:
    try:
        n=int(input("Ingrese un numero entero: "))
        a=False
    except:
        print("Vuelva a ingresar el valor")

if a==False:
    digitos=len(str(n))
    print("Su numero tiene {} digitos".format(digitos))