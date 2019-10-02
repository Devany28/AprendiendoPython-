#PROGRAMA ACUMULADO
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Declaramos variables Acumulado como int el 0 sera como un contador que ira
#aumentando con el ciclo que utilizaremos y la variable Numero como string
#las "" sera un espacio para el numero que nos de el usuario
Acumulado = int(0)
Numero = str("")

#Utilizaremos un ciclo while donde sera un ciclo infinito mientras la funcion se siga cumpliendo
#dentro del while ira un if
while True:
#con la funcion input le pedimos el valor al usuario
    Numero = input("Dame un numero entero: \n")
#Ahora con la funcion if si Numero es igual a las "" vacias ahi parara el ciclo con la instruccion break
    if Numero == "":
        print("Vacio. Salida del programa.")
        break
#Si el usuario sigue dando valores estos se iran acumulando (sumando) y se mostrara como salida
#el resultado del monto acumulado
    else:
        Acumulado+=int(Numero)
        Salida = "Monto Acumulado: {}"
        print(Salida.format(Acumulado))

    
