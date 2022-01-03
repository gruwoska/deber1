# El IMC resulta de la división de la masa del individuo (en kilogramos) entre el cuadrado de la estatura (en metros). El índice de masa corporal es un indicador del peso de una persona en relación con su altura.
# Clasificación del IMC de acuerdo con la OMS de la ONU:
# a. Menor a 16: Criterio de ingreso. b. 16 a 16.9: infra peso.
# c. 17 a 18.4: bajo peso.
# d. 18.5 a 24.9: peso normal.
# e. 25 a 29.9: sobrepeso.
# f. 30 a 34.9: obesidad pre-mórbida.
# g. 40 a 45: obesidad mórbida.
# h. Mayor a 45: obesidad híper-mórbida.
# Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor de IMC de la persona y la categoría en la cual fue clasificado.
pesoenlibras=float(input("ingrese su peso en libras:"))
estaturaencentimetros=float(input("Ingrese su estatura en centimentros:"))
def conversion1(pes):
    return pes*0.453592
def conversion2(est):
    return est/100
def icm(estatura,peso):
    estatura=estatura*estatura
    return peso/estatura
pesoenkilos=conversion1(pesoenlibras)
print("Su peso en kilos es {}".format(pesoenkilos))
estaturaenmetros=conversion2(estaturaencentimetros)
estaturaenmetros=estaturaenmetros*estaturaenmetros
rango=pesoenkilos/estaturaenmetros
print("Su valor de IMC es:{} ".format(rango))
if rango<16:
    print("Su categoria es: Criterio de ingreso")
if rango>=16 and rango<=16.9:
    print("Su categoria es: Infrapeso")
if rango>=17 and rango<=18.4:
    print("Su categoria es: Bajo peso")
if rango>=18.5 and rango<=24.9:
    print("Su categoria es: Peso normal")
if rango>=25 and rango<=29.9:
    print("Su categoria es: Sobrepeso")
if rango>=30 and rango<=34.9:
    print("Su categoria es: Obesidad premorbida")
if rango>=35 and rango<=45:
    print("Su categoria es :Obesidad morbida")
if rango>45:
    print("Su categoria es: Obesidad hiper-morbida")