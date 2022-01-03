
# Escriba una acción (MillasAKilometros) que convierta una distancia en millas a kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre ellas y debe retornar la distancia entre las ciudades en kilómetros.
# Desarrolle además una acción principal en donde utilice a la acción MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares de ciudades suministradas por el usuario.
# Entrada:
# Cuidad A
# Ciudad B
# 332
# Salida:
# Entre la Ciudad A y la Ciudad B hay 534.30 Km.
ciudadA=str(input("Ingrese el nombre de la ciudad A: "))
ciudadB=str(input("Ingrese el nombre de la ciudad B: "))
distanciaenmillas=float(input("Ingrese la distancia en millas entre las dos ciudades"))
def convertir(distancia):
    return distancia*1.60935
print("La distancia entre {} y {} es de {} km".format(ciudadA,ciudadB,convertir(distanciaenmillas)))
