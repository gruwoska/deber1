# Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
# anúmero.
a=True
while a==True:
    try:
        num=int(input("Ingrese un numero del 1 al 12: "))
        if num==0 or num>12:
            print("Vuelva a ingresar el valor")
        else:
            a=False
    except:
        print("Vuelva a ingresar el valor")

mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print("El mes que ingresó fue {} ".format(mes[num-1]))
