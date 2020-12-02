def check_valid_password(policy, password):
	first_pos = policy['first_pos'] - 1
	second_pos = policy['second_pos'] - 1
	letter = policy['letter']
	
	if (password[first_pos] == letter and password[second_pos] != letter) or (password[first_pos] != letter and password[second_pos] == letter):
		return True
	else:
		return False

valid_passwords = 0

with open('input.txt') as fd:
	for line in fd.readlines():
		policy = {}
		policy['letter'] = line.split(':')[0].split(' ')[1]
		policy['first_pos'] = int(line.split(':')[0].split(' ')[0].split('-')[0])
		policy['second_pos'] = int(line.split(':')[0].split(' ')[0].split('-')[1])
		
		password = line.split(':')[1].strip()
		
		if check_valid_password(policy, password):
			valid_passwords += 1
			
	print(valid_passwords)
		