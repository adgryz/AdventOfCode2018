polymer =  open('input_5_5.txt').readline()

alphabetTuples = [ (str(chr(i)),str(chr(i-32))) for i in range(97,123)]

alphabetPairs = [str(chr(i)) + str(chr(i-32)) for i in range(97,123)]
reversedAlphabetPairs = [pair[::-1] for pair in alphabetPairs]
allPairs = alphabetPairs + reversedAlphabetPairs

originalPolymer = polymer
shortestPolymerLen = 100000


for letterTuple in alphabetTuples:
  polymer = polymer.replace(letterTuple[0], '')
  polymer = polymer.replace(letterTuple[1], '')
  polymerLen = len(polymer)
  while True:
    for pair in allPairs:
      polymer = polymer.replace(pair, '')
    newLen = len(polymer)
    if polymerLen == newLen:
      break
    else:
      polymerLen = newLen
  shortestPolymerLen = min( len(polymer), shortestPolymerLen)
  polymer = originalPolymer

print(shortestPolymerLen)