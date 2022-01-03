
# Cree un algoritmo que tome por entrada las horas y 
# minutos de un día y 
# dé como resultado su equivalente en segundos.
a=int(input("Ingrese la hora: "))
b=int(input("Ingrese los minutos: "))
def conversiondehora(num):
    return num*3600
def conversiondeminuto(nam):
    return nam*60
def suma(uno,dos):
    return uno+dos
a=conversiondehora(a)
b=conversiondeminuto(b)
total=suma(a,b)
print("El total de segundos es {}".format(total))