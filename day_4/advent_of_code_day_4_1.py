def is_passport_valid(passport):
	required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	if passport == None:
		return False
		
	for field in required_fields:
		if field not in passport:
			return False
			
	return True
	
valid_passports = 0
passport = {}
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
			
		for token in line.split(' '):
			if token != '':
				passport[token.split(':')[0]] = token.split(':')[1]
				
		if line == '' or i == (len(lines) - 1):
			if is_passport_valid(passport):
				valid_passports += 1
			passport = {}

print(valid_passports)