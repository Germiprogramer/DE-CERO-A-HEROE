from random import randint

while True:
    tableroajedrez =  [
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
    (tableroajedrez[x])[0] = chr(0x2656)
    (tableroajedrez[y])[1] = chr(0x2656)
    (tableroajedrez[z])[2] = chr(0x2656)
    (tableroajedrez[a])[0] = chr(0x265C)
    (tableroajedrez[b])[1] = chr(0x265C)
    (tableroajedrez[c])[2] = chr(0x265C)