def count_letters_in_password(password):
	letters = {}
	
	for i in password:
		if not i in letters:
			letters[i] = 0
			
		letters[i] = letters[i] + 1
		
	return letters
	
def check_valid_password(policy, password):
	letters = count_letters_in_password(password)
	
	letter = policy['letter']
	if letter in letters:
		letter_count = letters[letter]
	else:
		letter_count = 0
	
	if letter_count > policy['max_count'] or letter_count < policy['min_count']:
		return False
	else:
		return True


valid_passwords = 0

with open('input.txt') as fd:
	for line in fd.readlines():
		policy = {}
		policy['letter'] = line.split(':')[0].split(' ')[1]
		policy['min_count'] = int(line.split(':')[0].split(' ')[0].split('-')[0])
		policy['max_count'] = int(line.split(':')[0].split(' ')[0].split('-')[1])
		
		password = line.split(':')[1]
		
		if check_valid_password(policy, password):
			valid_passwords += 1
			
	print(valid_passwords)
		