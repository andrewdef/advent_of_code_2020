import math

timestamp = None
buses = []
with open('input.txt') as fd:
	lines = fd.readlines()
	
	timestamp = int(lines[0])
	for bus in lines[1].split(','):
		if bus != 'x':
			buses.append(int(bus))
		
earliest_timestamp = float("inf")
answer = 0
for bus in buses:
	first_timestamp = math.ceil(timestamp / bus) * bus

	if first_timestamp < earliest_timestamp:
		earliest_timestamp = first_timestamp
		answer = bus * (earliest_timestamp - timestamp)
		
print(answer)
		
