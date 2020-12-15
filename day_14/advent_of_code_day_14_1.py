def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)
	
def apply_mask(mask, value):
	value_copy = value
	for i, c in enumerate(mask[::-1]):
		if c == '1':
			value_copy = set_bit(value_copy, i)
		elif c == '0':
			value_copy = clear_bit(value_copy, i)
			
	return value_copy

def decode_addresses(mask, original_address):
	value_copy = original_address
	floating_bits = []
	for i, c in enumerate(mask[::-1]):
		if c == '1':
			value_copy = set_bit(value_copy, i)
		elif c == 'X':
			floating_bits.append(i)
	
	addresses = [value_copy]
	for i in floating_bits:
		new_addresses = []
		for address in addresses:
			new_addresses.append(set_bit(address, i))
			new_addresses.append(clear_bit(address, i))
			
		addresses = new_addresses
	
	return addresses
	
program = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		instruction = ['', 0, 0]
		
		tokens = line.split(' ')
		if tokens[0] == 'mask':
			instruction[0] = 'mask'
			instruction[1] = tokens[2]
		else:
			instruction[0] = 'mem'
			instruction[1] = int(tokens[0].split('[')[1].replace(']', ''))
			instruction[2] = int(tokens[2])
		
		program.append(instruction)
	
memory = {}
current_mask = ''
for instruction in program:
	if instruction[0] == 'mask':
		current_mask = instruction[1]
	else:
		memory[instruction[1]] = apply_mask(current_mask, instruction[2])
		
sum = 0
for address, value in memory.items():
	sum += value
	
print(sum)