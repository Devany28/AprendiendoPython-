#PROGRAMA MULTIPLO
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Se declara la vaiable con la funcion int e input pidiendo al usuario un valor entero

Numero = int(input("Dame un numero entero: \n"))

#Se almacenan los valores en las variables como booleanos, si su residual es igual a cero
#el numero sera multiplo de cualquiera de los tres valores (3,5,7)

EsMultiplo3 = ((Numero%3)==0)
EsMultiplo5 = ((Numero%5)==0)
EsMultiplo7 = ((Numero%7)==0)

#Utilizaremos una funcion If donde se tendran que cumplir las condiciones, al poner AND
#todas las condiciones deben ser verdaderas en cuanto al OR la condicion es verdadera cuando una
#de ellas se cumple, los parentecis separan las condiciones dando a entender que las primeras dos
#van juntas y la tercera es individual 
if ((EsMultiplo3 and EsMultiplo5) or EsMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")

#En caso de que ninguna se cumpla el resultado sera incorrecto
