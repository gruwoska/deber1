# Dados N número positivos (N>1) 
# calcular el promedio de esta serie. Considere que la serie termina al leer un 0.
a=int(input("¿Cuantos numeros va a ingresar? "))
b=a
c=0
con=0
while a>0:
    
    num=float(input("Ingrese el numero: "))
    if num==0:
        b=con
        break
    c=num+c
    con=con+1
    a-=1
if c==0:
    c=1
prom=c/b
print("El promedio de los numeros ingresados es {}".format(prom))
