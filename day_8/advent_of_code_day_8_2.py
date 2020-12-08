def execute_program(instructions):
	accumulator = 0
	already_executed = []
	ip = 0
			
	while( True ):
		if ip in already_executed:
			return (False, accumulator)
		else:
			already_executed.append(ip)
		
		if ip >= len(instructions):
			break

		instruction = instructions[ip]
		opcode = instruction[0]
		
		if opcode == 'nop':
			ip += 1
		elif opcode == 'acc':
			accumulator += instruction[1]
			ip += 1
		elif opcode == 'jmp':
			ip += instruction[1]
			
	return (True, accumulator)

def replace_instruction(program, replacement, ip):
	instruction = program[ip]
	instruction = (replacement, instruction[1])
		
	program_copy = program.copy()
	program_copy[i] = instruction
	
	return program_copy

program = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		program.append((line.split(' ')[0], int(line.split(' ')[1])))
		
for i in range(0, len(program)):
	instruction = program[i]
	
	if instruction[0] in ('nop', 'jmp'):
		if instruction[0] == 'nop':
			program_copy = replace_instruction(program, 'jmp', i)
		else:
			program_copy = replace_instruction(program, 'nop', i)
		
		terminated, accumulator = execute_program(program_copy)
		
		if terminated:
			print(accumulator)
			exit			