lines = [line.rstrip('\n').split(',') for line in open('input_6.txt')]
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

def findClosestCord(x,y):
    minDist = 100000
    closestCord = -1
    occurences = 1
    for i in range(cordsNo):
        cord = cords[i]
        dist = distToCord(x,y,cord)
        if dist < minDist:
            minDist = dist
            closestCord = i+1
            occurences = 1
        elif dist == minDist:
            occurences += 1
    return  closestCord  if occurences == 1 else -1

areaSizes  = [0]*cordsNo
for x in range(size):
    for y in range(size):
        closestCord = findClosestCord(x,y)
        manhattanArray[x][y] = closestCord
        if closestCord != -1:
            areaSizes[closestCord-1] += 1

infiniteAreaCords = set()

for i in range(size):
    infiniteAreaCords.add(manhattanArray[i][0])
    infiniteAreaCords.add(manhattanArray[0][i])
    infiniteAreaCords.add(manhattanArray[i][size-1])
    infiniteAreaCords.add(manhattanArray[size-1][i])
infiniteAreaCords.remove(-1)

for inf in infiniteAreaCords:
    areaSizes[inf-1] = 0

result = max(areaSizes)
print(result)
