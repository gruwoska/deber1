# Dados tres (3) números, 
# Hacer una aplicación que calcule la resolvente.

from math import sqrt
brd=False
while brd==False: 
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese un numero: "))
    c=int(input("Ingrese un numero: "))
    p=pow(b,2)-4*a*c
    if p>0:
        d=sqrt(p)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a)
        print(x1,x2)
        brd=True
    else:
        print("Vuelva a ingresar otros valores")
        print(p)
