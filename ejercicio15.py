# Para un valor entero positivo que representa una 
# cantidad en segundos, 
# indicar su equivalente en minutos, horas y días.

a=False
while a==False:
    try:
        var=int(input("Ingrese los segundos: "))
        if var>-1:
            a=True
        else:
            print("Vuelva a ingresar el valor")
    except:
        print("Vuelva a ingresar el valor")
def conversionaminutos(num):
    return num/60
def conversionahoras(num1):
    return num1/3600
def conversionadias(num2):
    return num2/86400    
minutos=conversionaminutos(var)
hora=conversionahoras(var)
dias=conversionadias(var)
print("{} segundos tiene {} minutos".format(var,minutos))
print("{} segundos tiene {} horas".format(var,hora))
print("{} segundos tiene {} dias".format(var,dias))