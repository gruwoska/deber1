# Todos los años que se dividen exactamente entre 400, 
# o que son divisibles exactamente entre 4 y 
# no son divisibles exactamente entre 100 son años bisiestos. 
# Usando estas premisas crea un algoritmo que lea una
#  fecha como un número entero con el formato ddmmaaaa,
#   y luego extraiga el año 
# de la fecha indicando si el mismo es un año bisiesto o no.

fecha=''
while len(fecha)!=8:
    fecha=list(str(input("Ingrese el ddmmaaaa: ")))

año1=[]
a=1
for i in fecha:
    if a>4:
        año1.append(i)
    a+=1
b=[int(x) for x in año1]
uno=b[0]
dos=b[1]
tres=b[2]
cuatro=b[3]
for i in range(4):
    if i==0:
        lista1=[1000,2000,3000,4000,5000,6000,7000,8000,9000]
        variable1=lista1[uno-1]
    if i==1:
        lista2=[0,100,200,300,400,500,600,700,800,900] 
        variable2=lista2[dos] 
    if i==2:
        lista3=[0,10,20,30,40,50,60,70,80,90]
        variable3=lista3[tres] 
    if i==3:
        lista4=[0,1,2,3,4,5,6,7,8,9]
        variable4=lista4[cuatro]
año=variable4+variable3+variable2+variable1 
if año % 4 != 0: #no divisible entre 4
	print("El año {} no es un año bisiesto".format(año))
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("El año {} es un año bisiesto".format(año))
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("El año {} no es un año bisiesto".format(año))
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("El año {} es un año bisiesto".format(año))