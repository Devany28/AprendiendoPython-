#PROGRAMA TABLAS
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Utilizaremos la funcion for donde i (primer valor) varia en cada iteracion
#y le asignaremos un rango
for i in range(1,11):
#Declaramos una variable llamada Encabezado la cual identificara la tabla realizada
    Encabezado = "Tabla del {}"
#Con .format damos el valor a las llaves, dentro de el se encuentra i
#la cual ira aumentado mientras este dentro del rango dado
    print(Encabezado.format(i))
    print()
#Dentro de la funcion For utilizaremos otro For donde ahora j (segundo valor) sera la que varia en cada iteracion
#y tambien le asignando un rango
    for j in range(1,11):
#Declararemos la variable salida en la cual se llevara acabo la operacion donde se multiplicara
#el valor de i por el valor de j
        Salida = "{} x {} = {}"
#Damos el valor a las {} con .format
        print(Salida.format(i,j,i*j))
#Utilizaremos el else para terminar con el ciclo de la funcion
    else:
        print()
