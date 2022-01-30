import numpy as np

def readFile():
    matrix = []
    file = input("Introduce el nombre del archivo: ")
    if ".txt" not in file:
        file += '.txt'
    try:
        f = open(file, "r")
        for line in f:
            values = list(line.replace(" ", "").rstrip('\n'))
            values = list(map(int, values))
            matrix.append(values)
        f.close()
    except FileNotFoundError:
        print("Archivo no encontrado \n")
    return np.asarray(matrix)

def showLightbulb(room):
    print()
    while 0 in room:
        if room.size == 0:
            print("Debes cargar el archivo")
        x, y = getPosition(room)
        room = updateLighted(room, x, y)
        room[x , y] = 3
    
    print(str(room).replace(' [', '').replace('[', '').replace(']', '').replace('3', 'B').replace('2', '0').replace(' ', '  '))
    print("1. Exportar a .txt")
    print("2. Exportar a .csv")
    print("Presiona cualquier otra tecla para continuar")
    opt = input()
    try:
        opt = int(opt)
    except ValueError:
        opt = 3
    if opt == 1:
        text = str(room).replace(' [', '').replace('[', '').replace(']', '').replace('3', 'B').replace('2', '0').replace(' ', '  ')
        exportFile('.txt', text)
    elif opt == 2:
        text = str(room).replace(' [', '').replace('[', '').replace(']', '').replace('3', 'B').replace('2', '0').replace(' ', ',')
        exportFile('.csv', text)


def getPosition(room):
    max = -1
    x = 0
    y = 0
    for row in range(len(room)):
        for col in range(len(room[row])):
            lightBulbs = 0
            if room[row,col] == 0:
                lists = [room[row+1:,col], room[:row,col][::-1], room[row,col+1:], room[row,:col][::-1]]
                for i in lists:
                    for j in i:
                        if j != 0:
                            break
                        lightBulbs += 1
                if lightBulbs > max:
                    x, y = row,col
                    max = lightBulbs
    return x,y

def updateLighted(matrix, x, y):
    movement = -1
    while movement <= 1:
        row = x + movement
        while row>=0 and row<len(matrix):
            if(matrix[row][y] != 0):
                break
            matrix[row][y] = 2
            row += movement
        movement += 2
    movement = -1
    while movement <= 1:
        col = y + movement
        while col>=0 and col<len(matrix[x]):
            if(matrix[x][col] != 0):
                break
            matrix[x][col] = 2
            col += movement
        movement += 2
    return matrix

def exportFile(extension, room):
    name = input("Ingresa el nombre del archivo: ")
    f = open(name + extension, "w")
    f.write(room)
    f.close()
    print("Archivo exportado correctamente \n")

room = np.array([])
op = 0
while op != 3:
    print("1. Cargar habitacion")
    print("2. Mostar colocacion de bombillos")
    print("3. Salir")
    op = input()
    try:
        op = int(op)
    except ValueError:
        print("Opcion no valida")
        op = 3
    if op == 1:
        room = readFile()
        print()
    elif op == 2:
        showLightbulb(room)
    elif op!=3:
        print("Opcion no valida")
