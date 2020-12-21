def sort_ingredient(ingredient):
	return ingredient[1]
	
all_ingredients = {}
all_allergens = {}
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for line in lines:
		line = line.strip()
		
		tokens = line.split('(')
		
		food = list(map(str.strip, tokens[0].strip().split(' ')))
		
		if len(tokens) == 2:
			allergens = list(map(str.strip, tokens[1].replace(')', '').replace(',', '').split(' ')))
			allergens.remove('contains')
			
			for allergen in allergens:
				if not allergen in all_allergens:
					all_allergens[allergen] = []
					
				all_allergens[allergen].append(food)
				
			for ingredient in food:
				if ingredient not in all_ingredients:
					all_ingredients[ingredient] = [[], 0]
					
				for allergen in allergens:
					if allergen not in all_ingredients[ingredient][0]:
						all_ingredients[ingredient][0].append(allergen)
						
				all_ingredients[ingredient][1] += 1
			
answer = 0
for ingredient in all_ingredients:
	for possible_allergen in all_ingredients[ingredient][0].copy():
		for food in all_allergens[possible_allergen]:
			if ingredient not in food and possible_allergen in all_ingredients[ingredient][0]:
				all_ingredients[ingredient][0].remove(possible_allergen)
				break
	
	if len(all_ingredients[ingredient][0]) == 0:
		answer += all_ingredients[ingredient][1]

print(answer)

