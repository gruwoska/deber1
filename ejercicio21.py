# En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario
valor=float(input("Ingrese el valor de su compra:"))
if valor>1000:
    descuento=valor*0.2
    total=valor-descuento
else:
    total=valor
print("El valor total a pagar es {}".format(total))