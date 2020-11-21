valor1 = int(input("Ingrese el primer valor"))
valor2 = int(input("Ingrese el segundo valor"))

if valor1 > valor2:
    print("El primer valor {} es MAYOR".format(valor1))
else:
    if valor1 == valor2:
        print("Ambos número son iguales")
    else:
        print("El segundo valor {} es MENOR".format(valor1))


