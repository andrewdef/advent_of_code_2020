total_answers = 0
group_answers = {}
group_size = 0
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		if line != '':
			group_size += 1
			for answer in line:
				if answer not in group_answers:
					group_answers[answer] = 1
				else:
					group_answers[answer] += 1
					
		if line == '' or i == (len(lines) - 1):
			for answer in group_answers:
				if group_answers[answer] == group_size:
					total_answers += 1
					
			group_answers = {}
			group_size = 0

print(total_answers)