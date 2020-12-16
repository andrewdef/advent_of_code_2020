def is_valid_field(value, rules):
	for field_name, ranges in rules.items():
		for range in ranges:
			if value >= range[0] and value <= range[1]:
				return True
		
	return False
	
def find_possible_field_pos(value, rules):
	candidates = []
	for field_name, ranges in rules.items():
		for range in ranges:
			if value >= range[0] and value <= range[1]:
				candidates.append(field_name)
		
	return candidates
	
my_ticket = []
nearby_tickets = []
rules = {}
section = ''
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		if line == '':
			continue
		
		if line in ['your ticket:', 'nearby tickets:']:
			section = line
		else:
			if section == '':
				tokens = line.split(':')
				
				range_tokens = tokens[1].strip().split(' ')
				ranges = []
				ranges.append(list(map(int, range_tokens[0].split('-'))))
				ranges.append(list(map(int, range_tokens[2].split('-'))))
				
				rules[tokens[0]] = ranges
			else:
				ticket = list(map(int, line.split(',')))
				
				if section == 'your ticket:':
					my_ticket = ticket
				else:
					nearby_tickets.append(ticket)			
	
field_map = {}
for i, x in enumerate(my_ticket):
	field_map[i] = [field_name for field_name in rules.keys()]
	
valid_tickets = []
for ticket in nearby_tickets:
	is_valid_ticket = True
	for field in ticket:
		if not is_valid_field(field, rules):
			is_valid_ticket = False
			break
			
	if is_valid_ticket:
		valid_tickets.append(ticket)
		
for field_pos in field_map.keys():
	for ticket in valid_tickets:
		candidates = find_possible_field_pos(ticket[field_pos], rules)
		field_map[field_pos] = list(set(field_map[field_pos]) & set(candidates))

unknown_fields = -1
while( unknown_fields != 0 ):
	unknown_fields = 0
	for field_pos in field_map.keys():
		if len(field_map[field_pos]) == 1:
			value_to_remove = field_map[field_pos][0]
			
			for i in range(0, len(my_ticket)):
				if i != field_pos and value_to_remove in field_map[i]:
					field_map[i].remove(value_to_remove)
		else:
			unknown_fields += 1
			
field_map = dict([(field_pos, field_names[0]) for field_pos, field_names in field_map.items()])
answer = 1
for field_pos, field_name in field_map.items():
	if field_name.split(' ')[0] == 'departure':
		answer *= my_ticket[field_pos]
print(answer)