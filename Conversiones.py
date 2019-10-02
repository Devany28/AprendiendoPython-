#PROGRAMA DE CONVERSIONES
#Arevalo Chavez Devany Yazmin
#Fecha de creacion: 25/09/2019

# Para comenzar declararemos una variable de tipo Str (texto),
# asignandole una cadena con los siguientes digitos "1234".

Numero = "1234"

# El comando Type nos permite saber el tipo de la variable anterior,
# junto al comando print nos mostrara el resultado en la consola

print(type(Numero))

# Al correr el programa el resultado que nos tiene que dar seria una
# variable tipo string

#--------------------------------------------------------

# Ahora declararemos la variable (Numero) a tipo Int

Numero = int(Numero)

print(type(Numero))

# Como se puede notar la variable a cambiado a tipo Int (Entero)

#--------------------------------------------------------

# Las llaves se utilizan para guardar el espacio de un resultado

Salida = "El numero utilizado es {}"

# Para dar salida imprimiendo el numero dado en la variable
# utilizaremos .format

print(Salida.format(Numero))
