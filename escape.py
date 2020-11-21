#Carlos Torres 26/10/2020

import sys

#Defino las variables 
gravedad = float(sys.argv[1])
radio = float(sys.argv[2])*1000

#Valida los datos y cálcula la velocidad de escape del planeta
if gravedad > 0 and radio >0:
    velocidad = (2*gravedad*radio)**(1/2)
    print("La velocidad minima para salir del planeta es {} m/s".format(velocidad))
else:
    print("Verifique los datos ingresados, debe introducir valores númericos positivos")
