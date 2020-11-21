password = input("Ingrese Clave: ")

letras = 0 

for c in password:
    if c.isalpha():
        letras += 1 

if letras < 6:
    print("Su password DEBE tener 6 o más letras")
else: 
    print("En su password HAY al menos 6 letras") 
