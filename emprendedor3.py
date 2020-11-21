#Carlos Torres 26/10/2020

#Se debe ingresar el ["Precio","Número de usuarios totales","Gastos","Utilidad Anterior"]

import sys

#Visualizo lo datos ingresados
print(sys.argv)

precio_venta = float(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = float(sys.argv[3])

#Valido el número de argumentos que ingreso el usuario
if len(sys.argv) == 5:
    ulitidad_ant = float(sys.argv[4])
else:
    ulitidad_ant = 1000 

#Cálculo la utilidad del año actual
utilidad = (precio_venta*usuarios) - gastos
utilidad_bruta = utilidad*(0.65)

#Cálculo de la razón (Utilidad actual / Utilidad anterior)
if utilidad > 0:
    razon_utilidades = (utilidad_bruta/ulitidad_ant)
    
else:
    razon_utilidades = (utilidad/ulitidad_ant)
    
#informo la razón cálculada
print("La razón entre la ulitidad actual y la del año anterior es {}".format(razon_utilidades))

