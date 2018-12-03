frequencies = [int(line.rstrip('\n')) for line in open('input_1_5.txt')]
count = len(frequencies)

summ = 0
i = 0

buffor = 100000
maxcount = 1000000
results = [buffor]*maxcount

while i<maxcount:
	summ += frequencies[i % count]
	results[summ] += 1
	if results[summ] == buffor + 2:
		print(summ)
		break
	i+=1