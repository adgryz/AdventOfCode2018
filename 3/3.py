claims = [line.rstrip('\n') for line in open('input_3.txt')]

def parse(input):
    (dists,dims) = tuple(input.split(' ')[-2:])
    (left,top) = dists[:-1].split(',')
    (width,height) = dims.split('x')
    return (int(left),int(top), int(width), int(height))

parsedClaims = [parse(claim) for claim in claims]

size = 1000
fabric = [ [0 for j in range(size)] for i in range(size)]

conflicts = 0

for claim in parsedClaims:
    (left,top,width,height) = claim
    for x in range(left, left+width):
        for y in range(top, top+height):
            fabric[x][y]+=1

for line in fabric:
    for cell in line:
        if cell > 1:
            conflicts+=1       

print(conflicts)