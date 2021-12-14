print("""
A nuestros queridos Kevin y Stuart les encanta jugar con palabras.
Kevin hará subpalabras a partir de vocales.
Stuart hará subpalabras a partir de consonantes.
""")


PALABRA = input("Elige una palabra: ")
try:
    PALABRA = str(PALABRA)
except:
    pass

#vocales
PUNTOS_KEVIN = 0
#consonantes
PUNTOS_STUART = 0
print("La longitud de la palabra es {}".format(len(PALABRA)))
print("\n")

LISTAVOCALES = ["A","E","I","O","U","a","e","i","o","u"]

for posicionletra in range(len(PALABRA)):
    if PALABRA[posicionletra] in LISTAVOCALES:
        PUNTOS_KEVIN += int(len(PALABRA)-posicionletra)

    elif PALABRA[posicionletra] not in LISTAVOCALES:
        PUNTOS_STUART += int(len(PALABRA)-posicionletra)
        
print("los puntos de kevin son {}".format(PUNTOS_KEVIN))
print("los puntos de stuart son {}".format(PUNTOS_STUART))
print("\n")


if PUNTOS_STUART > PUNTOS_KEVIN:
    print("gana Stuart con {} puntos".format(PUNTOS_STUART))
elif PUNTOS_KEVIN > PUNTOS_STUART:
    print("gana Kevin con {} puntos".format(PUNTOS_KEVIN))
else:
    print("Empate técnico mister")
