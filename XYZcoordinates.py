import numpy as np

#this method reads coordinate data from gipsy files
def getCoord(f):
    file = open(f, 'r')

    lines = file.readlines()

    k = 0
    for line in range(1, len(lines)):
        if lines[line][7:8] == ' ':
            k = line
            break

    coordinates = []

    for i in range(1, k, 3):
        xyz = []
        for j in range(3):
            if lines[i+j][25:26] == "-":
                xyz.append(float(lines[i+j][25: 47]))
            else:
                xyz.append(float(lines[i + j][26: 47]))
        coordinates.append(xyz)

    file.close()

    coordinates = np.array(coordinates)

    return coordinates

a = getCoord('PZITRF08001.00X')
print(a)