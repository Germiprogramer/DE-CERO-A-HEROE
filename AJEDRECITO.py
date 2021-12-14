from random import randint

def encerrada(FILA, COLUMNA):
    if FILA == 0 and tablero[FILA + 1][COLUMNA] != ' ':
        fallo = True
    elif FILA == 1:
        if tablero[FILA + 1][COLUMNA] != ' ' and tablero[FILA - 1][COLUMNA] != ' ':
            fallo = True
        else:
            fallo = False
    elif FILA == 2 and tablero[FILA - 1][COLUMNA] != ' ':
            fallo = True
    else:
        fallo = False
    return fallo

def printeartablero(tablero):
    contador_indice = 0
    for tablero[contador_indice] in tablero:
        print(tablero[contador_indice])
        contador_indice += 1
    print("\n")


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

    #blancas
    (tablero[x])[0] = chr(0x2656)
    (tablero[y])[1] = chr(0x2656)
    (tablero[z])[2] = chr(0x2656)
    #negras
    (tablero[a])[0] = chr(0x265C)
    (tablero[b])[1] = chr(0x265C)
    (tablero[c])[2] = chr(0x265C)

    printeartablero(tablero)

    ENCERRADAx = encerrada(x, 0)
    ENCERRADAy = encerrada(y, 1)
    ENCERRADAz = encerrada(z, 2)
    ENCERRADAa = encerrada(a, 0)
    ENCERRADAb = encerrada(b, 1)
    ENCERRADAc = encerrada(c, 2)

    if ENCERRADAx == True and ENCERRADAy == True and ENCERRADAz == True:
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
        pass
    elif ENCERRADAa == True and ENCERRADAb == True and ENCERRADAc == True:
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
        pass
    else:
        break

turno = randint(0, 1)
while True:
    if turno == 1:
        if ENCERRADAx == False and ENCERRADAa == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            ENCERRADAa = encerrada(a, 0)
        elif ENCERRADAy == False and ENCERRADAb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            ENCERRADAb = encerrada(b, 1)
        elif ENCERRADAz == False and ENCERRADAc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            ENCERRADAc = encerrada(c, 2)
        elif ENCERRADAx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            ENCERRADAa = encerrada(a, 0)
        elif ENCERRADAy == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            ENCERRADAb = encerrada(b, 1)
        elif ENCERRADAz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            ENCERRADAc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if ENCERRADAa == False and ENCERRADAx == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            ENCERRADAx = encerrada(x, 0)
        elif ENCERRADAb == False and ENCERRADAy == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            ENCERRADAy = encerrada(y, 1)
        elif ENCERRADAc == False and ENCERRADAz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            ENCERRADAz = encerrada(z, 2)
        elif ENCERRADAa == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            ENCERRADAx = encerrada(x, 0)
        elif ENCERRADAb == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            ENCERRADAy = encerrada(y, 1)
        elif ENCERRADAc == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            ENCERRADAc = encerrada(z, 2)
        else:
            break
        turno = 1
    printeartablero(tablero)

printeartablero(tablero)
if ENCERRADAx == True and ENCERRADAy == True and ENCERRADAz == True:
    print("Ninguna pieza blanca se puede mover, han ganado las negras")
elif ENCERRADAa == True and ENCERRADAb == True and ENCERRADAc == True:
    print("Ninguna pieza negra se puede mover, han ganado las blancas")

#curiosamente, al ejecutar, las piezas blancas aparecen como negras, y las negras como blancas
        
        