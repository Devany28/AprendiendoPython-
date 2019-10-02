def TIEMPO(Distancia,Velocidad):
    tiempo = Distancia / Velocidad
    return tiempo

Distancia = int(input("Dame un valor para la distancia: "))
Velocidad = int(input("Dame un valor para la velocidad: "))
Resultado = TIEMPO(Distancia,Velocidad)
print("El tiempo que tomara recorrer una distancia de {} y una velocidad de {} es de {} Hrs".format(Distancia,Velocidad,Resultado))
