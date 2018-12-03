ids = [line.rstrip('\n') for line in open('input_2_5.txt')]
idLen = len(ids[0])

def findDiffOne():
    for id1 in ids:
        for id2 in ids:
            if id1 != id2:
                errors = 0
                for i in range(idLen):
                    if id1[i] != id2[i]:
                        errors+=1
                        if errors == 2:
                            break
                if errors == 1:
                    return(id1,id2)

def extractSame(id1, id2):
    common = []
    for i in range(idLen):
        if id1[i] == id2[i]:
            common.append(id1[i])
    return ''.join(common)

matchingIds = findDiffOne()
print(extractSame(*matchingIds))        