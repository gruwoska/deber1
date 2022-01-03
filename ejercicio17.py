# En un estacionamiento el monto a pagar se calcula multiplicando el número de horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
# Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada y la hora de salida de un vehículo (las mismas corresponden a un mismo día) calcule el monto a pagar por el dueño del vehículo.
# La entrada vendrá dada por dos enteros positivos el primero representa las horas y el segundo los minutos, además por último se debe leer un carácter (A o P) que indica si la hora es AM o PM.
print("Ingrese la hora con minutos de entrada porfavor")
def conversion(num):
    return num/60
horadeentrada=int(input("Hora: "))
minutosdeentrada=int(input("minutos: "))
minutosdeentrada=conversion(minutosdeentrada)
ampm1=str("AM o PM: ")
print("Ingrese la hora con minutos de salida porfavor")
horadesalida=int(input("Hora:"))
minutosdeesalida=int(input("minutos:"))
minutosdeesalida=conversion(minutosdeesalida)
entrada=horadeentrada+minutosdeentrada
salida=horadesalida+minutosdeesalida
totaldehoras=salida-entrada
mediahora=totaldehoras-int(totaldehoras)
mediahora=mediahora*60
totaldehoras=int(totaldehoras)
valorapagar=totaldehoras*4
valorapagar2=mediahora*2.5
total=valorapagar+valorapagar2
print("El valor a pagar es de {}".format(total))