trees = 1
slopes = [(3, 1)]
map = []

def count_trees(map, x_slope, y_slope):
	x = 0
	y = 0
	trees_in_map = 0
	
	while( True ):
		x += x_slope
		y += y_slope
		
		if y >= len(map):
			break

		line = map[y]
		
		x_pos = x % len(line)

		if line[x_pos] == '#':
			trees_in_map += 1

	return trees_in_map

with open('input.txt') as fd:
	for line in fd.readlines():
		line = line.strip()
		map.append(line)

for slope in slopes:
	trees *= count_trees(map, slope[0], slope[1])
	
print(trees)