#Carlos Torres 26/10/2020

#Se debe ingresar el ["Precio","Número de usuarios","Gastos"]

import sys

#Visualizo los valores ingresados
print(sys.argv)

#Determino las variables
precio_venta = float(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = float(sys.argv[3])

#Cálculo la utilidad neta y bruta
utilidad = (precio_venta*usuarios) - gastos
utilidad_bruta = utilidad*(0.65)

#informo utilidad o perdida
if utilidad > 0:
    print("Su utilidad es {} USD".format(utilidad_bruta))
else:
    print("Su perdida es {} USD".format(utilidad))