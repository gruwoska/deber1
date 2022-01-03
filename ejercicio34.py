# Escriba una función que calcule el perímetro del pentágono 
# (siendo el perímetro la suma de los lados del polígono)
def perimetro(l):
    return 5*l
lado=float(input("Ingrese el valor del lado: "))
print("El perimetro es {}".format(perimetro(lado)))