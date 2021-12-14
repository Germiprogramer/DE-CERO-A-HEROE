PALABRA = input("Elige una palabra: ")

#vocales
PUNTOS_KEVIN = 0
#consonantes
PUNTOS_STUART = 0
print(len(PALABRA))

LISTAVOCALES = ["A","E","I","O","U","a","e","i","o","u"]

for posicionletra in range(len(PALABRA)):
    if PALABRA[posicionletra] in LISTAVOCALES:
        PUNTOS_KEVIN += int(len(PALABRA)-posicionletra)
        

    elif PALABRA[posicionletra] not in LISTAVOCALES:
        PUNTOS_STUART += int(len(PALABRA)-posicionletra)
        
print("los puntos de kevin")

if PUNTOS_STUART > PUNTOS_KEVIN:
    print("gana Stuart con {} puntos".format(PUNTOS_STUART))
elif PUNTOS_KEVIN > PUNTOS_STUART:
    print("gana Kevin con {} puntos".format(PUNTOS_KEVIN))
else:
    print("Empate técnico mister")
