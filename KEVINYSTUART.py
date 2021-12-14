PALABRA = input("Elige una palabra: ")

PUNTOS_STUART = 0
PUNTOS_KEVIN = 0

LISTAVOCALES = ["A","E","I","O","U","a","e","i","o","u"]

for posicionletra in range(len(PALABRA)):
    if posicionletra in LISTAVOCALES:
        print(PALABRA[posicionletra:len[PALABRA]])
    elif posicionletra not in LISTAVOCALES:
        print(PALABRA[posicionletra:len[PALABRA]])




if PUNTOS_STUART > PUNTOS_KEVIN:
    print("gana Sturat")
elif PUNTOS_KEVIN > PUNTOS_STUART:
    print("gana Kevin")
else:
    print("Empate técnico mister")
