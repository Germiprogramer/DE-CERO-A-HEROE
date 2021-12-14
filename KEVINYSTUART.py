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
        print(len(PALABRA)-posicionletra)

    elif PALABRA[posicionletra] in LISTAVOCALES:
        PUNTOS_STUART += int(len(PALABRA)-posicionletra)
        print(len(PALABRA)-posicionletra)
        

if PUNTOS_STUART > PUNTOS_KEVIN:
    print("gana Sturat")
elif PUNTOS_KEVIN > PUNTOS_STUART:
    print("gana Kevin")
else:
    print("Empate técnico mister")
