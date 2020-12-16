def is_valid_field(value, rules):
	for field_name, ranges in rules.items():
		for range in ranges:
			if value >= range[0] and value <= range[1]:
				return True
		
	return False
	
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
	
error_rate = 0
for ticket in nearby_tickets:
	for field in ticket:
		if not is_valid_field(field, rules):
			error_rate += field
			
print(error_rate)