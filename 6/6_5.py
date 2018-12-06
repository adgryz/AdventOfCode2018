lines = [line.rstrip('\n').split(',') for line in open('input_6_5.txt')]
cords = [(int(cord[1]), int(cord[0]) ) for  cord in lines]

cordsNo = len(cords)
size = 400
manhattanArray = [[0]*size for _ in range(size)]

def print2d(list):
    for i in range(size):
        print(list[i])

for i in range(cordsNo):
    (x,y) = cords[i]
    manhattanArray[x][y] = i+1

def distToCord(x,y,cord):
    return abs(x-cord[0]) + abs(y-cord[1])

def countDistances(x,y):
    sumDist = 0
    for cord in cords:
        sumDist += distToCord(x,y,cord)
    return  sumDist

safeAreaSize = 0
maxSize = 10000
for x in range(size):
    for y in range(size):
        dist = countDistances(x,y)
        if dist < maxSize:
            safeAreaSize += 1
        manhattanArray[x][y] = 1 if dist < maxSize else 0

print(safeAreaSize)