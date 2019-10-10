#Devany Yazmin Arevalo Chavez

Precios = []

for i in range(10):
    Valor=float(input("Dame un precio: "))
    Precios.append(Valor)
    Suma = sum(Precios)
print("Los precios dados son ${}" .format(Precios))
print("La suma de los precios dados es ${}" .format(Suma))

def Promedio(Precios):
	Suma=0
	for Valor in Precios:
		Suma+=Valor
	Cantidad = len(Precios)
	return Suma/float(Cantidad)
Promedio = (Promedio(Precios))
print("El promedio es {}" .format(Promedio))

import statistics as stats
DesviacionEst =(stats.pstdev(Precios))
print("La division estandar es {}" .format(DesviacionEst))

PrecioMax = Promedio + DesviacionEst
PrecioMin = Promedio - DesviacionEst

print("El precio maximo es $%0.2f"%PrecioMax)
print("El precio minimo es $%0.2f"%PrecioMin)





