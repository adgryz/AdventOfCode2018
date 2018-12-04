from datetime import datetime
lines = [line.rstrip('\n').split(']') for line in open('input_4_5.txt')]

def parseLine(line):
    dateStr = line[0][1:]
    parsedDate = datetime.strptime(dateStr, '%Y-%m-%d %H:%M')
    parsedInfo = parseInfo(line[1])
    return (parsedDate, parsedInfo)

def parseInfo(info):
    keyword = info.split(' ')[2]
    if(keyword == 'up'):
        return True
    elif(keyword == 'asleep'):
        return False
    else :
        return int(keyword[1:])
    

parsedLines = [parseLine(line) for line in lines]
sortedLines = sorted(parsedLines, key=lambda x: x[0])

def increaseTimesInArr(min,max,arr):
    for i in range(min,max):
        arr[i] += 1
    return arr

# Finding max sleeping guard
guards = {}
currentGuardId = -1
feltAsleepAt = None
for record in sortedLines:
    if isinstance(record[1], bool) == False:
        currentGuardId = record[1]
        if currentGuardId not in guards:
            guards[currentGuardId] = [0]*60
    elif record[1] == False:
        feltAsleepAt = record[0].minute
    elif record[1] == True:
        awakenAt = record[0].minute
        guards[currentGuardId] = increaseTimesInArr(feltAsleepAt,awakenAt, guards[currentGuardId])

maxGuardsMinutes = [(guard,max(guards[guard])) for guard in guards]
maxGuard = max(maxGuardsMinutes, key=lambda x:x[1])
(maxGuardId, maxMinutes) = maxGuard
minuteNo = guards[maxGuardId].index(maxMinutes)
result = maxGuardId * minuteNo
print(result)