import functools
frequencies = [int(line.rstrip('\n')) for line in open('input_1.txt')]
result = functools.reduce(lambda a, b: a+b, frequencies)
print(result)
