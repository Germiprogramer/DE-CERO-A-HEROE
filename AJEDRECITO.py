from random import randint

def printeartablero(tablero):
    contador_indice=0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1
    print("\n")

def encerrada(FILA,COLUMNA):
    if FILA == 0 and tablero[FILA+1][COLUMNA] != ' ':
        fallo = True
    elif FILA == 1:
        if tablero[FILA+1][COLUMNA] != ' ':
            tablero[FILA-1][COLUMNA] = tablero[FILA][COLUMNA]
            tablero[FILA][COLUMNA] = ' '
        else:
            tablero[FILA+1][COLUMNA] = tablero[FILA][COLUMNA]
            tablero[FILA][COLUMNA] = ' '
    elif FILA == 2 and tablero[FILA-1][COLUMNA] != ' ':
        fallo = True
    else:
        fallo = True
    return fallo

def movimiento(FILA, COLUMNA):
    if FILA == 0:
        tablero[FILA+1][COLUMNA] = tablero[FILA][COLUMNA]
        tablero[FILA][COLUMNA] = ' '
    elif FILA == 1:
        if tablero[FILA+1][COLUMNA] != ' ':
            tablero[FILA-1][COLUMNA] = tablero[FILA][COLUMNA]
            tablero[FILA][COLUMNA] = ' '
        else:
            tablero[FILA+1][COLUMNA] = tablero[FILA][COLUMNA]
            tablero[FILA][COLUMNA] = ' '
    elif FILA == 2:
        tablero[FILA-1][COLUMNA] = tablero[FILA][COLUMNA]
        tablero[FILA][COLUMNA] = ' '

def cambio(FILA, COLUMNA):
    if FILA == 0:
        FILA += 1
    elif FILA == 1:
        if tablero[FILA+1][COLUMNA] != ' ':
            FILA -= 1
        else:
            FILA += 1
    elif FILA == 2:
        FILA -= 1
    return FILA

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
    #blancas
    (tablero[x])[0] = chr(0x2656)
    (tablero[y])[1] = chr(0x2656)
    (tablero[z])[2] = chr(0x2656)
    #negras
    (tablero[a])[0] = chr(0x265C)
    (tablero[b])[1] = chr(0x265C)
    (tablero[c])[2] = chr(0x265C)

    printeartablero(tablero)

    ENCERRADAx = encerrada(x,0)
    ENCERRADAy = encerrada(y,1)
    ENCERRADAz = encerrada(x,2)
    ENCERRADAa = encerrada(a,0)
    ENCERRADAb = encerrada(b,1)
    ENCERRADAc = encerrada(c,2)

    if ENCERRADAx == True and ENCERRADAy == True and ENCERRADAz == True:
        print("El jugador blanco no se puede mover, volvemos a generar el tablero")
        pass
    elif ENCERRADAa == True and ENCERRADAb == True and ENCERRADAc == True:
        print("El jugador negro no se puede mover, volvemos a generar el tablero")
        pass
    else:
        break

