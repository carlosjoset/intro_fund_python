#Carlos Torres 26/10/2020
#Cargado al GIT

#Se debe ingresar el ["Precio","Número de usuarios totales","Número de usuarios premium","Numero de usuario gratuitos","Gastos"]

import sys

#Visualizo los valores ingresados
print(sys.argv)

precio_venta = float(sys.argv[1])
usuarios = int(sys.argv[2])
usuarios_premium = int(sys.argv[3])
usuarios_gratuitos = int(sys.argv[4])
gastos = float(sys.argv[5])

#Determino los usuarios normales
usuarios_nomales = usuarios - usuarios_premium - usuarios_gratuitos

#Cálculo de la utilidad neta y bruta
utilidad = precio_venta*(2*usuarios_premium + usuarios_nomales) - gastos
utilidad_bruta = utilidad*(0.65)

#informo la utilidad o la perdida
if utilidad > 0: 
    print("Su utilidad es {} USD".format(utilidad_bruta))
else:
    print("Su perdida es {} USD".format(utilidad))

