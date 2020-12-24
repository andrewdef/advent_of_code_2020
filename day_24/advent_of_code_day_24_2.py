def follow_direction(direction):
	ns = 0
	ew = 0
	
	for way in direction:
		if way == 'e':
			ew += 1
		elif way == 'w':
			ew -= 1
		elif way == 'se':
			ew += 1
			ns -= 1
		elif way == 'sw':
			ns -= 1			
		elif way == 'ne':
			ns += 1		
		elif way == 'nw':
			ew -= 1
			ns += 1					
		
	return (ew, ns)

def parse_line(line):
	i = 0
	direction = []
	while( i < len(line) ):
		if line[i] == 'n' or line[i] == 's':
			direction.append(line[i:i+2])
			i += 2
		else:
			direction.append(line[i])
			i += 1
	
	return direction
	
def count_adjacent_tiles(tile):
	adjacent_offsets = [(-1, 1), (0, 1), (1, 0), (1, -1), (0, -1), (-1, 0)]
	return_values = {'w' : 0, 'b' : 0}
	
	for offset in adjacent_offsets:
		adj_tile = (tile[0] + offset[0], tile[1] + offset[1])
		
		if adj_tile in grid:
			return_values[grid[adj_tile]] += 1
			
	return return_values		
	
directions = []
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for line in lines:
		line = line.strip()
		
		directions.append(parse_line(line))
		
assert follow_direction(parse_line('nwwswee')) == (0, 0)

grid = {}
for i in range(-100, 100):
	for k in range(-100, 100):
		grid[(i, k)] = 'w'

for direction in directions:
	tile_coordinates = follow_direction(direction)
	
	if not tile_coordinates in grid:
		grid[tile_coordinates] = 'w'
		
	if grid[tile_coordinates] == 'b':
		grid[tile_coordinates] = 'w'
	else:
		grid[tile_coordinates] = 'b'
		
for day in range(0, 100):
	to_flip = {}
	for tile, color in grid.items():
		adj_tiles = count_adjacent_tiles(tile)
		
		if color == 'b' and (adj_tiles['b'] == 0 or adj_tiles['b'] > 2):
			to_flip[tile] = 'w'
		elif color == 'w' and adj_tiles['b'] == 2:
			to_flip[tile] = 'b'
			
	for tile, color in to_flip.items():
		grid[tile] = color

print(sum([tile == 'b' for coordinate, tile in grid.items()]))
		
		
