# Dados tres números enteros positivos A, B y C,
#  determine ¿cuál de ellos es el mayor? y 
# ¿cuál es el segundo mayor?
a=False
while a==False:
    try:
        var1=int(input("Ingrese un numero entero positivo: "))
        var2=int(input("Ingrese un numero entero positivo: "))
        var3=int(input("Ingrese un numero entero positivo: "))
        if var1>0 and var2>0 and var3>0:
            if var1!=var2 and var1!=var3 and var2!=var3:
                a=True
            else:
                print("Ha introducido valores repetidos, porfavor vuelva a ingresar los valores por favor")
        else:
            print("Vuelva a ingresar los valores por favor")
    except:
        print("Vuelva a ingresar los valores por favor")
lista=[var1,var2,var3]
mayor1=max(lista)
lista.remove(mayor1)
mayor2=max(lista)
print("El mayor es {} y le sigue el {}".format(mayor1,mayor2))

