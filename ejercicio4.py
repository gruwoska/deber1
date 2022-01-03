# Dados dos (2) números 
# calcule la suma, resta, multiplicación, división y módulo.

a=float(input("Ingrese un numero"))
b=float(input("Ingrese un numero"))
def suma(num1,num2):
    return num1+num2

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    try:
        b=num1/num2
        return b
    except ZeroDivisionError:
         return ("No se puede dividir para cero")
def modulo(num1,num2):
    return num1%num2
print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,b))
print(modulo(a,b))
