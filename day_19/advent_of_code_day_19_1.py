def strip(s):
	return s.strip().strip('\"')

def match(string_to_check, rule, current_position, rules):
	new_position = current_position
	if rule[0] in ['a', 'b']:
		if current_position >= len(string_to_check) or string_to_check[current_position] != rule[0]:
			return False
		elif len(rule) == 1:
			if current_position == (len(string_to_check) - 1):
				return True
			else:
				return False
			
		new_position += 1
		
		return match(string_to_check, rule[1:], new_position, rules)
	else:
		for alternative in rules[rule[0]]:
			if match(string_to_check, alternative + rule[1:], new_position, rules):
				return True
				
		return False				

rules = {}
strings_to_check = []
after_blank = False
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for line in lines:
		if line == '\n':
			after_blank = True
			continue
		elif after_blank:
			strings_to_check.append(line.replace('\n', ''))
		else:			
			tokens = line.split(':')
			rules[tokens[0]] = [list(map(strip, x.split(' '))) for x in map(strip, tokens[1].split('|'))]
	
print(sum([match(s, ['0'], 0, rules) for s in strings_to_check]))
