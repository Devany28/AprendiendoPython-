#PROGRAMA COMPARA
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019 

#Declaramos dos variables donde utilizamos la funcion input para pedir un valor al usuario
Numero1 = input("Inserta el primer numero: \n")
Numero2 = input("Inserta el segundo numero: \n")

#Declaramos la variable salida donde se mostraran los valores dados y sus comparaciones
Salida = "Numero proporcionados: {} y {}. {}."

#Primero utilizaremos la funcion If para comparar como iguales los valores dados 
if (Numero1 == Numero2):
#Si la funcion se cumple se imprimira el siguiente resultado
    print(Salida.format(Numero1,Numero2,"Los numero son iguales"))
#Si la funcion no se cumple se colocara otro if dentro del if donde compararemos cual valor es el mayor
else:
    if Numero1 > Numero2:
        print(Salida.format(Numero1,Numero2,"El mayor es el primero"))
    else:
        print(Salida.format(Numero1,Numero2,"El mayor es el segundo"))

#Al final se mostrara la salida mostrando los valores dados por el usuario junto a su comparacion
