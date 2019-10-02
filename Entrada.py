#PROGRAMA ENTRADA
#Arevalo Chavez Devany Yazmin 
#Fecha de creacion: 25/09/2019

#Declaramos una variable dando una funcion input la cual tendra un valor string

Entrada = input("Inserte un valor: \n")
print(type(Entrada))

#Con el siguiente comando verificaremos el numero dado si este lleva un punto
#significa que no es un valor entero si no un valor decimal (Float), con el
#usaremos un formato find si este retorna -1 significa que se encuentra un punto
#y el valor es decimal

EsEntero = (Entrada.isdigit() and Entrada.find(".")==-1)

#Si la variable EsEntero es verdadera pasara a la funcion If, imprimiendo como respuesta
#que el dato es entero

if (EsEntero):
    print("Dato entero. ¡Muy Bien!")
#Se utilizara un else en caso de que sea falso
else:
    print("El dato no es entero. Intente de nuevo.")
