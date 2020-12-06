total_answers = 0
group_answers = []

with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		if line != '':
			for answer in line:
				if answer not in group_answers:
					group_answers.append(answer)
					
		if line == '' or i == (len(lines) - 1):
			total_answers += len(group_answers)
			group_answers = []

print(total_answers)