# Dados dos (2) 
# lados de un triángulo en cm, 
# calcular la hipotenusa del mismo.
from math import sqrt
a=float(input("Ingrese el cateto a: "))
b=float(input("Ingrese el cateto b: "))
c=sqrt((pow(a,2)+(pow(b,2))))
print(c)