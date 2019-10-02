def NumeroMayor(Valor1, Valor2):
    if Valor1 > Valor2:
        return True

PrimerNum = int(input("Dame el primer numero enteros: "))
SegundoNum = int(input("Dame el segundo numero entero: "))
Resultado = NumeroMayor(PrimerNum, SegundoNum)

if Resultado == True:
    print("El numero mayor es: ")
    print(PrimerNum)
    
else:
    print("El numero mayor es: ")
    print(SegundoNum)
