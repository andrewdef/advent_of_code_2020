import re

def validate_numeric_field(passport, field, length=None, min_value=None, max_value=None):
	field_value = passport[field]
	field_name = field.upper()
	passport_id = passport['id']
	
	if not field_value.isnumeric() or (length != None and len(field_value) != length):
		print(f'Invalid value {field_value} for {field_name} in passport: {passport_id}')
		return False

	field_value = int(field_value)
	if min_value != None and field_value < min_value:
		print(f'Value {field_value} out of range for {field_name} in passport: {passport_id}')
		return False
	elif max_value != None and field_value > max_value:
		print(f'Value {field_value} out of range for {field_name} in passport: {passport_id}')
		return False
		
	return True
	
def validate_height_field(passport, field, limits):
	field_value = passport[field]
	field_name = field.upper()
	passport_id = passport['id']
	
	mu = field_value[-2:]
	value = field_value[0:-2]
	if mu not in limits:
		print(f'Invalid mu {mu} for field {field_name} in passport:  {passport_id}')
		return False
	elif not value.isnumeric():
		print(f'Invalid height value {value} for field {field_name} in passport:  {passport_id}')
		return False
		
	value = int(value)
	if value < limits[mu][0] or value > limits[mu][1]:
		print(f'Invalid height value {value} for field {field_name} in passport:  {passport_id}')
		return False

	return True

def validate_rgb_field(passport, field):
	field_value = passport[field]
	field_name = field.upper()
	passport_id = passport['id']
	
	if not re.match('#[0-9a-f]{6}', field_value):
		print(f'Invalid value {field_value} for {field_name} in passport: {passport_id}')
		return False
		
	return True
	
def valid_lov_field(passport, field, list_of_values):
	field_value = passport[field]
	field_name = field.upper()
	passport_id = passport['id']
	
	if field_value not in list_of_values:
		print(f'Invalid value {field_value} for {field_name} in passport: {passport_id}')
		return False
		
	return True
	
def is_passport_valid(passport):
	required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	passport_id = passport['id']
	
	for field in required_fields:
		if field not in passport:
			print(f'Missing field {field.upper()} in passport {passport_id}')
			return False
			
	if not validate_numeric_field(passport, 'byr', min_value=1920, max_value=2002):
		return False
	elif not validate_numeric_field(passport, 'iyr', min_value=2010, max_value=2020):
		return False
	elif not validate_numeric_field(passport, 'eyr', min_value=2020, max_value=2030):
		return False
	elif not validate_height_field(passport, 'hgt', {'cm': (150, 193), 'in': (59, 76)}):
		return False
	elif not validate_rgb_field(passport, 'hcl'):
		return False
	elif not valid_lov_field(passport, 'ecl', ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
		return False
	elif not validate_numeric_field(passport, 'pid', length=9):
		return False
		
	return True
	
valid_passports = 0
passport = {}
passport_sequence = 1
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
			
		for token in line.split(' '):
			if token != '':
				passport[token.split(':')[0]] = token.split(':')[1]
				
		if line == '' or i == (len(lines) - 1):
			passport['id'] = passport_sequence
			
			if is_passport_valid(passport):
				valid_passports += 1

			passport = {}
			passport_sequence += 1

print(valid_passports)