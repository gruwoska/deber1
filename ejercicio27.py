# Dada una secuencia de números terminada en cero (0), 
# elaborar un algoritmo que informe al usuario qué valor tiene el número mayor y qué valor tiene el número menor, 
# sin contar el cero (0).
a=[]
num=str(input("Ingrese una secuencia de numeros que termine en 0: "))
for i in num:
    if i=='0':
        pass
    else:
        a.append(int(i))
print("El numero mayor de la secuencia de numeros es {}".format(max(a)))
print("El numero menor sin contar el cero es {}".format(min(a)))