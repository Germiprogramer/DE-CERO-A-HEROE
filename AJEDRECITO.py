from random import randint

def printeartablero(tablero):
    contador_indice=0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1
    print("\n")

while True:
    tablero =  [
    [' ', ' ', ' '], 
    [' ', ' ', ' '],
    [' ', ' ', ' '], 
    ]

    x = randint(0,2)
    y = randint(0,2)
    z = randint(0,2)
    a = randint(0,2)
    b = randint(0,2)
    c = randint(0,2)

    while x == a:
        a = randint(0,2)
    while y == b:
        b = randint(0,2)
    while z == c:
        c = randint(0,2)

    #posicionpiezas
    (tablero[x])[0] = chr(0x2656)
    (tablero[y])[1] = chr(0x2656)
    (tablero[z])[2] = chr(0x2656)
    (tablero[a])[0] = chr(0x265C)
    (tablero[b])[1] = chr(0x265C)
    (tablero[c])[2] = chr(0x265C)

    printeartablero(tablero)