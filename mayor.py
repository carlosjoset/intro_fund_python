#Carlos Torres 28/10/2020

#El usuario debe ingresar 3 números  [n1, n2, n3, ...] y determinar el mayor.  

#Importando librerias 
import sys

"""Definiendo las variables. ADICIONAL: A pesar que no hemos visto el uso del "try except", lo investigué en internet 
con el fin de poder agregarle un mensaje en la terminal, en caso de que alguno de los argumentos no sean numéricos"""
  
try:
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    if n1 >= n2 and n1 >= n3:
        print(n1)
    elif n2 >= n1 and n2 >= n3:
        print(n2)
    else: 
        print(n3)
except:
    print("Argumentos inválidos: Debe ingresar 3 argumentos y numéricos")
