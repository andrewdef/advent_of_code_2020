numbers = {}
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		for k, number in enumerate(map(int, line.split(','))):
			numbers[number] = [k + 1]
			
	
turn = k + 2
last_spoken = number
while( True ):
	if len(numbers[last_spoken]) == 1:
		last_spoken = 0
	else:
		last_spoken = numbers[last_spoken][-1] - numbers[last_spoken][-2]
		
	if not last_spoken in numbers:
		numbers[last_spoken] = [turn]
	else:
		numbers[last_spoken].append(turn)
		
	if turn == 2020:
		print(last_spoken)
		break
		
	turn += 1