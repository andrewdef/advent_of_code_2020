def count_all_holdable_bags(source_color, rules):
	total_holdable_bags = 0
			
	for quantity, holdable_color in rules[source_color]:
		total_holdable_bags += quantity
		total_holdable_bags += (quantity * count_all_holdable_bags(holdable_color, rules))
					
	return total_holdable_bags

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
				quantity = int(tokens[i])
				rules[color].append((quantity, holdable_color))
				
				i += 4

print(count_all_holdable_bags('shiny gold', rules))
