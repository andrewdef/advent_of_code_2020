def calculate_score(deck):
	return sum([(i + 1) * card for i, card in enumerate(deck[-1::-1])])

def calculate_gamekey(deck1, deck2):
	return '-'.join(map(str, deck1)) + '/' + '-'.join(map(str, deck2))
	
def play(deck1, deck2, level, recursive_play_enabled):
	gamekey = calculate_gamekey(deck1, deck2)
	previous_result = previous_game_results.get(gamekey)
	
	if previous_result != None:
		return previous_result
		
	previous_rounds_decks = {}
	
	game_winner = None
	round = 1
	while (game_winner == None):
		roundkey = calculate_gamekey(deck1, deck2)
		
		if previous_rounds_decks.get(roundkey) != None:
			game_winner = 1
		else:
			previous_rounds_decks[roundkey] = round
				
			card1 = deck1[0]
			card2 = deck2[0]
			
			del deck1[0]
			del deck2[0]
			
			if recursive_play_enabled and card1 <= len(deck1) and card2 <= len(deck2):
				subgame_result = play(deck1.copy()[0:card1], deck2.copy()[0:card2], level + 1, recursive_play_enabled)
				winner = subgame_result[0]
			else:
				if card1 > card2:
					winner = 1
				else:
					winner = 2
			
			if winner == 1:
				deck1.append(card1)
				deck1.append(card2)
			else:
				deck2.append(card2)
				deck2.append(card1)
				
			if len(deck1) == 0:
				game_winner = 2
			elif len(deck2) == 0:
				game_winner = 1
				
			round += 1
			
	if game_winner == 1:
		result = (1, deck1)
	else:
		result = (2, deck2)
		
	previous_game_results[gamekey] = result
	return result
	
starting_deck1 = []
starting_deck2 = []
in_player_1 = False
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for line in lines:
		line = line.strip()
		
		if line == 'Player 1:':
			in_player_1 = True
		elif line == 'Player 2:':
			in_player_1 = False
		elif line == '':
			continue
		else:
			if in_player_1:
				starting_deck1.append(int(line))
			else:
				starting_deck2.append(int(line))
				
previous_game_results = {}
print(calculate_score(play(starting_deck1, starting_deck2, 0, False)[1]))
		
