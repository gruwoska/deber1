# Construya una función que solicite edades al usuario y determine 
# el promedio de las edades mayores a 18 años. 
# El usuario indicará cuando desea dejar de suministrar datos de entrada. 
# En la Acción Principal se informará el promedio calculado.
a=int(input("Ingrese cuantas edad va a ingresar: "))
print("Puede detener el programa escribiendo: DETENERSE")
def funcion(al):
    prom=0
    i=0
    while al>0:
        edad=str(input("Ingrese la edad: "))
        if edad.lower()=="detenerse":
            break
        else:
            edad=int(edad)
        if edad>18:
            prom+=int(edad)
            i+=1
    
        al-=1
    if prom!=0 and i!=0:
        prom=prom/i
        return(prom)
    else:
        return("No ha ingresado valores")
print(funcion(a))
    