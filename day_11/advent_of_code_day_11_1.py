def count_adjacent_occupied_seats(x, y, map, row):
	occupied_seats = 0
	
	adj = [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1, +1)]
	
	for a in adj:
		new_x = x + a[0]
		new_y = y + a[1]
		
		if new_x >= 0 and new_x < len(row) and new_y >= 0 and new_y < len(map):
			if map[new_y][new_x] == '#':
				occupied_seats += 1
				
	return occupied_seats
	
def count_occupied_seats(x, y, map, row):
	occupied_seats = 0
	
	adj = [(-1, -1), (0, -1), (+1, -1), (-1, 0), (+1, 0), (-1, +1), (0, +1), (+1, +1)]
	
	for a in adj:
		new_x = x
		new_y = y
		
		while( True ):
			new_x = new_x + a[0]
			new_y = new_y + a[1]
			
			if new_x >= 0 and new_x < len(row) and new_y >= 0 and new_y < len(map):
				if map[new_y][new_x] == '#':
					occupied_seats += 1
					break
				elif map[new_y][new_x] == 'L':
					break
			else:
				break
				
	return occupied_seats
	
map = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		map.append([x for x in line])

while( True ):
	occupied_seats = 0
	changes = 0
	
	map_copy = []
	for row in map:
		map_copy.append([x for x in row])
	
	for y, row in enumerate(map):
		for x, seat in enumerate(row):
			adjacent_occupied_seats = count_adjacent_occupied_seats(x, y, map, row)
			if adjacent_occupied_seats  == 0 and seat == 'L':
				map_copy[y][x] = '#'
				changes += 1
			elif adjacent_occupied_seats >= 4 and seat == '#':
				map_copy[y][x] = 'L'
				changes += 1
				
			if map_copy[y][x] == '#':
				occupied_seats += 1
	
	if changes == 0:
		break
	
	map = map_copy
		
print(occupied_seats)
	