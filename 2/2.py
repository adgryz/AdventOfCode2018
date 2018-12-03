ids = [line.rstrip('\n') for line in open('input_2.txt')]

doubles = 0
triples = 0

def checkId(id):
    lettersCount = [0]*30
    for letter in id:
        index = ord(letter)-97
        lettersCount[index]+=1
    isDouble = 2 in lettersCount
    isTriple = 3 in lettersCount
    return (isDouble, isTriple)

for id in ids:
    (isDouble, isTriple) = checkId(id)
    if(isDouble): 
        doubles+=1
    if(isTriple):
        triples+=1

print(doubles*triples)
