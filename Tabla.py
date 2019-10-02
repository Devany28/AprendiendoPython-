#PROGRAMA TABLA
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Asignamos una variable con funcion input dandole un mensaje al usuario
Numero = input("Dame un numero del 1 al 9: \n")

#Asignamos la variable Numero con tipo de dato Int (Entero)
Numero = int(Numero)

#Utilizamos la funcion For donde i varia en cada iteracion
#seguido de un in donde se le asignara un rango
for i in range(1,11):
#Declaramos la variable salida donde se llevara acabo la operacion de la multiplicacion de i * numero
    Salida = "{} x {} = {}"
#Para finalizar madandamos imprimir el resultado utilizando .format para dar los valores a las llaves
    print(Salida.format(Numero,i,i*Numero))

    
