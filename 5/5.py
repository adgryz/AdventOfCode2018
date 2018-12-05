polymer =  open('input_5.txt').readline()

alphabet = [str(chr(i)) + str(chr(i-32)) for i in range(97,123)]
reversedAlphabet = [pair[::-1] for pair in alphabet]
allPairs = alphabet + reversedAlphabet
polymerLen = len(polymer)

while True:
  for pair in allPairs:
    polymer = polymer.replace(pair, '')
  newLen = len(polymer)
  if polymerLen == newLen:
    break
  else:
    polymerLen = newLen

print(polymerLen)