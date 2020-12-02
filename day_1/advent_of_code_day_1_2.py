numbers = []

with open('input.txt') as fd:
	for line in fd.readlines():
		number = int(line)
		numbers.append(number)
		
for i in range(0, len(numbers)):
	for j in range(i + 1, len(numbers)):
		for k in range(i + 2, len(numbers)):
			if numbers[i] + numbers[j] + numbers[k] == 2020:
				print(numbers[i] * numbers[j] * numbers[k])
				break

		