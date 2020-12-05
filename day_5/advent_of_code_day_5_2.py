import math

def binary_partition(sequence, high, low, letter_high, letter_low):
	ret_value = -1
	
	for i, letter in enumerate(sequence):
		if i == (len(sequence) - 1):
			if letter == letter_low:
				ret_value = low
			else:
				ret_value = high
		else:
			if letter == letter_low:
				high = low + math.floor((high - low) / 2)
			else:
				low = high - math.floor((high - low) / 2)
				
	return ret_value	
				
def calculate_seat_id(boarding_pass):
	row = binary_partition(boarding_pass[0:7], 127, 0, 'B', 'F')
	column = binary_partition(boarding_pass[7:], 7, 0, 'R', 'L')

	return (row * 8 + column)
	
all_ids = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
			
		all_ids.append(calculate_seat_id(line))

all_ids = sorted(all_ids)

for i in range(1, len(all_ids)):
	id = all_ids[i]
	
	if id - 2 == all_ids[i - 1]:
		print(id - 1)