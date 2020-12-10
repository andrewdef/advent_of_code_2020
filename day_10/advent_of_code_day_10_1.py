adapters = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		adapters.append(int(line))

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

counts = {}
for i in range(1, len(adapters)):
	diff = adapters[i] - adapters[i - 1]
	
	if diff not in counts:
		counts[diff] = 0
		
	counts[diff] += 1
		
print(counts[1] * counts[3])
	