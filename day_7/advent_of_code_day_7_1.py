def can_contain_bag_color(source_color, destination_color, rules):
	to_check = [source_color]
	
	while ( len(to_check) != 0) :
		new_to_check = []
		
		for color in to_check:
			for holdable_color in rules[color]:
				if holdable_color == destination_color:
					return True
				else:
					new_to_check.append(holdable_color)
					
		to_check = new_to_check
		
	return False

rules = {}
eligible_colors = 0
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		tokens = line.split(' ')
		color = tokens[0] + ' ' + tokens[1]
		rules[color] = []
		
		if tokens[4] != 'no':
			i = 4
			
			while( i < len(tokens) ):
				holdable_color = tokens[i + 1] + ' ' + tokens[i + 2]
				rules[color].append(holdable_color)
				
				i += 4

for color in rules:
	if can_contain_bag_color(color, 'shiny gold', rules):
		eligible_colors += 1

print(eligible_colors)