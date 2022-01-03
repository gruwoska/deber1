# Construya una función “Eleva” 
# Que reciba como parámetros una base y un exponente y 
# retorne al algoritmo principal el resultado 
# de elevar un numero al otro.
base=int(input("Ingrese la base: "))
expo=int(input("Ingrese el exponente: "))
def eleva(bas,exp):
    c=1
    while exp>0:
        c=bas*c
        exp=exp-1
    return c
print(eleva(base,expo))