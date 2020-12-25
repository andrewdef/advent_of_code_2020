import math

def chinese_remainder(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total
	
buses = []
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for i, bus in enumerate(lines[1].split(',')):
		if bus != 'x':
			buses.append((int(bus) - i, int(bus)))

print(chinese_remainder(buses))