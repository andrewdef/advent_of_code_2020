def do_math(left_term, operator, right_term):
	if operator == '*':
		return left_term * right_term
	elif operator == '+':
		return left_term + right_term
	else:
		raise Exception('Unknown operator: ' + operator)
	
def is_operator(c, operator_priorities):
	for operators in operator_priorities:
		if c in operators:
			return True
			
	return False
	
def evaluate_expression(expression, operator_priorities):
	in_parenthesis = 0
	subexpression = None
	
	terms = []
	for c in expression:
		term = None
		
		if c == ' ':
			continue		
		elif c == ')':
			in_parenthesis -= 1
			if in_parenthesis == 0:
				term = evaluate_expression(' '.join(subexpression), operator_priorities)
			else:
				subexpression.append(c)
		elif c == '(':
			in_parenthesis += 1
			if in_parenthesis == 1:
				subexpression = []
			else:
				subexpression.append(c)
		elif in_parenthesis != 0:
			subexpression.append(c)
		elif is_operator(c, operator_priorities):
			term = c
		elif c.isdigit():
			term = int(c)
		else:
			raise Exception("Unknown symbol in expression: " + c)
			
		if term != None:
			terms.append(term)
	
	for operators in operator_priorities:
		left_term = None
		right_term = None
		operator = ''
		
		new_terms = []
		for i, term in enumerate(terms):
			if is_operator(term, operator_priorities):
				operator = term
			else:
				if left_term == None:
					left_term = term
				else:
					right_term = term
					
			if left_term != None and right_term != None:
				if operator in operators:
					left_term = do_math(left_term, operator, right_term)
					right_term = None
				else:
					new_terms.append(left_term)
					new_terms.append(operator)
					
					left_term = right_term
					right_term = None
					
		if left_term != None:
			new_terms.append(left_term)
			
		terms = new_terms
			
	return terms[0]			
	
sum = 0
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for line in lines:
		sum += evaluate_expression(line.strip(), [['+'], ['*']])
		
print(sum)
