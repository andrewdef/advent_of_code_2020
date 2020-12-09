def is_sum_of_preamble(number, preamble):
	for i in range(0, len(preamble)):
		for k in range(i + 1, len(preamble)):
			if (preamble[i] + preamble[k]) == number:
				return True
	
	return False
	
numbers = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		numbers.append(int(line))
		
for i in range(25, len(numbers)):
	if not is_sum_of_preamble(numbers[i], numbers[i - 25:i]):
		print(numbers[i])
		break