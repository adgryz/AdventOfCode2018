claims = [line.rstrip('\n') for line in open('input_3_5.txt')]
claimsNo = len(claims)
claimsWithoutConflict = [True]*(claimsNo+1)
claimsWithoutConflict[0] = False

def parse(input):
    splitted = input.split(' ')
    id = splitted[0][1:]
    (dists,dims) = tuple(splitted[-2:])
    (left,top) = dists[:-1].split(',')
    (width,height) = dims.split('x')
    return (int(left),int(top), int(width), int(height), int(id))

parsedClaims = [parse(claim) for claim in claims]

size = 1000
fabric = [ [0 for j in range(size)] for i in range(size)]

for claim in parsedClaims:
    (left,top,width,height,id) = claim
    for x in range(left, left+width):
        for y in range(top, top+height):
            if fabric[x][y] != 0:
                claimsWithoutConflict[id] = False
                claimsWithoutConflict[fabric[x][y]] = False
            fabric[x][y]=id
    

print(claimsWithoutConflict.index(True))