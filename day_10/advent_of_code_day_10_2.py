from functools import lru_cache

@lru_cache
def count_valid_arrangements(start_index):
	if start_index == len(adapters) - 1:
		return 1

	valid = 0
	for k in range(1, 4):
		if (start_index + k) < len(adapters):
			diff = adapters[start_index + k] - adapters[start_index] 
			if diff <= 3:
				valid += count_valid_arrangements(start_index + k)
				
	return valid
	
adapters = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		adapters.append(int(line))

adapters.append(0)
adapters.append(max(adapters) + 3)

adapters.sort()

print(count_valid_arrangements(0))
	