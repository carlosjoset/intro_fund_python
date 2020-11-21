#Carlos Torres 28/10/2020

#El usuario debe ingresar su jugada de "Piedra" "Papel" o "Tijera" ["Jugada"]

#Importando librerias 
import sys
import random

#Determino las variables
jugada_cpu = random.randint(1,3)
jugada_usr = sys.argv[1]

#Convierto y valido la variable introducida por el usuario en una equilavente en número 
if jugada_usr == "tijera":
    jugada_usr_int = 1
elif jugada_usr == "papel":
    jugada_usr_int = 2
elif jugada_usr == "piedra":
    jugada_usr_int = 3
else:
    jugada_usr_int = "Argumento inválido: Debe ser piedra, papel o tijera" 

#Definio las combinatoria del del juego y sus resultados
if jugada_cpu == 1 and jugada_usr_int == 1: 
    print("Computador juega tijera")
    print("Empataste")
elif jugada_cpu == 2 and jugada_usr_int == 2:   
    print("Computador juega papel")
    print("Empataste")
elif jugada_cpu == 3 and jugada_usr_int == 3:
    print("Computador juega piedra")
    print("Empataste")
elif jugada_cpu == 1 and jugada_usr_int == 2:
    print("Computador juega tijera")
    print("Perdiste")
elif jugada_cpu == 1 and jugada_usr_int == 3:
    print("Computador juega tijera")
    print("Ganaste")
elif jugada_cpu == 2 and jugada_usr_int == 1:
    print("Computador juega papel")
    print("Ganaste")
elif jugada_cpu == 2 and jugada_usr_int == 3:
    print("Computador juega papel")
    print("Perdiste")
elif jugada_cpu == 3 and jugada_usr_int == 1: 
    print("Computador juega piedra")
    print("Perdiste")
elif jugada_cpu == 3 and jugada_usr_int == 2:
    print("Computador juega piedra")
    print("Ganaste")
else:
    print(jugada_usr_int)



