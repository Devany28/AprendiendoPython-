#PROGRAMA NOMBRE
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

#Declaramos dos variables con la funcion input pidiendo al usuaro su nombre y sus apellidos
Nombre = input("Ingresa tu nombre \n")
Apellidos = input("Ingresa tus apellidos \n")

#Al colocar las " " se realiza la concatenacion (une las variables) de los valores tipos String
NombreCompleto = Nombre+" "+Apellidos

#Con el formato .upper el valor de la variable cambiara a mayusculas
NombreCompleto = NombreCompleto.upper()

#Para finalizar imprimimos el resultado
print(NombreCompleto)
