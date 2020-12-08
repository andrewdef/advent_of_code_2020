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
			ip += int(instruction[1])
			
	return (True, accumulator)

program = []
with open('input.txt') as fd:
	lines = fd.readlines()
	for i, line in enumerate(lines):
		line = line.strip()
		
		program.append((line.split(' ')[0], int(line.split(' ')[1])))
		
terminated, accumulator = execute_program(program)
print(accumulator)