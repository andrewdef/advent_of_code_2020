import math
def turn(current_direction, angle):
	directions = ['N', 'E', 'S', 'W']
	
	ticks = (angle / 90) % 4
	
	return directions[int((directions.index(current_direction) + ticks) % len(directions))]

directions = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		directions.append((line[0], int(line[1:])))
		
north_south_ship = 0
east_west_ship = 0
current_direction = 'E'

for direction in directions:
	command = direction[0]
	unit = direction[1]
	
	if command == 'F':
		command = current_direction
	
	if command == 'N':
		north_south_ship += unit
	elif command == 'S':
		north_south_ship -= unit
	elif command == 'E':
		east_west_ship += unit
	elif command == 'W':
		east_west_ship -= unit
	elif command == 'R':
		current_direction = turn(current_direction, unit)
	elif command == 'L':
		current_direction = turn(current_direction, -unit)
	
assert turn('E', 180) == 'W'
assert turn('N', 360) == 'N'
assert turn('S', -90) == 'E'
assert turn('E', -270) == 'S'

print(abs(north_south_ship) + abs(east_west_ship))