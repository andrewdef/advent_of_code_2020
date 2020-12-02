numbers = []

with open('input.txt') as fd:
	for line in fd.readlines():
		number = int(line)
		numbers.append(number)
		
for i in range(0, len(numbers)):
	for j in range(i + 1, len(numbers)):
		if numbers[i] + numbers[j] == 2020:
			print(numbers[i] * numbers[j])
			break

		