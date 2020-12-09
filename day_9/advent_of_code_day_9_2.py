def is_sum_of_preamble(number, numbers):
	for i in range(0, len(numbers)):
		for k in range(i + 1, len(numbers)):
			if (numbers[i] + numbers[k]) == number:
				return True
	
	return False
	
numbers = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		numbers.append(int(line))
		
target = -1
for i in range(25, len(numbers)):
	if not is_sum_of_preamble(numbers[i], numbers[i - 25:i]):
		target = numbers[i]
		break
		
answer = None
i = 0
while( answer == None and i < len(numbers) ):
	sum = 0
	k = 0
	members = []
	
	while( sum < target ):
		sum += numbers[i + k]
		members.append(numbers[i + k])
		k += 1
		
		if sum == target:
			answer = min(members) + max(members)
	
	i += 1

print(answer)