#Dado un número entero cuya cantidad de dígitos es igual a 5, 
# determine si es capicúa.
c=0
while c==0:
    a=str(input("Ingrese un numero de 5 digitos: "))
    a=list(a)
    if len(a)==5:
        b=a[::-1]
        if a==b:
         print("Si es un numero capicua")
         c=c+1
        else:
          print("No es un numero capicua")
    else:
        print("Ingrese un numero de 5 digitos por favor")
