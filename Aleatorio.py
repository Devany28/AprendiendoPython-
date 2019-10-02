#PROGRAMA TIPO ALEATORIO
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Para este programa utilizaremos librerias llamadas Modules
#Para utilizar dicho modulo tenemos que importarlo utilizando "import"

import random

#Definiremos la variable Numero1 como tipo Float
#(Flotante, numeros con decimales) asignandole un numero cualquiera

Numero1 = float(10.5)

#Ahora utilizaremos una una funcion, las cuales se encargan de realizar una determinada tarea,
#utilizaremos la funcion llamada def, le asignamos un nombre seguido de ():

def MiFuncion():
#Dentro de esta funcion declararemos una variable llamada Numero2 como Float a la cual se le
#asignara un numero aleatorio el cual sera asignado por random.randrange 
    Numero2 = float(random.randrange(1,10))
#Declararemos una variable a la cual se le asigna un mensaje el cual al imprimirlo nos mostrara el resultado,
#Utilizamos {} para separar el lugar y los asignamos con .format
    Mensaje = "La suma de {} y {} es {}"
    print(Mensaje.format(Numero1,Numero2,Numero1+Numero2))

MiFuncion()
