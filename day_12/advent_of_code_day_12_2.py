import math
def turn(x, y, angle):
	radians = math.radians(angle)
	ox = 0
	oy = 0

	qx = ox + math.cos(radians) * (x - ox) + math.sin(radians) * (y - oy)
	qy = oy + -math.sin(radians) * (x - ox) + math.cos(radians) * (y - oy)

	return round(qx), round(qy)

directions = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		directions.append((line[0], int(line[1:])))
		
north_south_wp = 1
east_west_wp = 10
current_direction_wp = 'E'
north_south_ship = 0
east_west_ship = 0
for direction in directions:
	command = direction[0]
	unit = direction[1]
	
	if command == 'N':
		north_south_wp += unit
	elif command == 'S':
		north_south_wp -= unit
	elif command == 'E':
		east_west_wp += unit
	elif command == 'W':
		east_west_wp -= unit
	elif command == 'R':
		east_west_wp, north_south_wp = turn(east_west_wp, north_south_wp, unit)
	elif command == 'L':
		east_west_wp, north_south_wp = turn(east_west_wp, north_south_wp, -unit)
	elif command == 'F':
		north_south_ship += north_south_wp * unit
		east_west_ship += east_west_wp * unit
	
print(abs(north_south_ship) + abs(east_west_ship))