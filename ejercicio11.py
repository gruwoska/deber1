# Dado un (1) número de cuatro (4) dígitos imprimirlo por 
# separado en unidades, decenas, centenas y unidades de mil.
b=True
while b==True:
    try:
        a=int(input("Ingrese un numero entero de cuatro digitos: "))
        if len(str(a))==4:    
          b=False
        else:
            print("No ha ingresado un numero entero de cuatro digitos")      
    except:
        print("No ha ingresado un numero entero de cuatro digitos")
a=str(a)        
print("Unidad:{}".format(a[3]))
print("Decena:{}".format(a[2]))
print("Centena:{}".format(a[1]))
print("Unidad de mil: {}".format(a[0]))
print("El programa ha terminado")