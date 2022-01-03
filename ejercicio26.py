# Dado un número entero N que representa una contraseña y asumiendo que una contraseña debe tener al menos 10 dígitos para ser segura, 
# determine si la contraseña ingresada por el usuario es correcta, 
# de no serlo debe pedirla nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta mostrar un mensaje de éxito al usuario, por salida estándar.
a=True
while a==True:
    try:
        num=int(input("Ingrese una contraseña que tenga al menos 10 digitos"))
        if len(str(num))>=10:
            print("Su contraseña es segura")
            a=False
        else:
            print("Ha introducido una contraseña incorrecta")
            print("Ingrese una nueva contraseña por favor")
    except:
        print("Ha introducido una contraseña incorrecta")
        print("Ingrese una nueva contraseña por favor")


