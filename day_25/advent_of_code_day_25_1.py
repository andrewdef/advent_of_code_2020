import math

#Implementation taken from https://www.geeksforgeeks.org/discrete-logarithm-find-integer-k-ak-congruent-modulo-b/
def powmod(x, y, p):  
  
    res = 1; # Initialize result  
  
    x = x % p;
  
    while (y > 0):  
        if (y & 1):  
            res = (res * x) % p;  
  
        y = y >> 1;
        x = (x * x) % p;  
    return res;  
  
#Implementation taken from https://www.geeksforgeeks.org/discrete-logarithm-find-integer-k-ak-congruent-modulo-b/
def discrete_logarithm(a, b, m):  
    n = int(math.sqrt(m) + 1);  
  
    value = [0] * m;  
  
    for i in range(n, 0, -1):  
        value[ powmod (a, i * n, m) ] = i;  
  
    for j in range(n):  
        cur = (powmod (a, j, m) * b) % m;  
  
        if (value[cur]):  
            ans = value[cur] * n - j;  
              
            if (ans < m):  
                return ans;  
      
    return -1;  
	
card_public_key = 0
door_public_key = 0
with open('input.txt') as fd:
	lines = fd.readlines()
	
	for i, line in enumerate(lines):
		line = line.strip()
		
		if i == 0:
			card_public_key = int(line)
		else:
			door_public_key = int(line)

card_loop_size = discrete_logarithm(7, card_public_key, 20201227)
door_loop_size = discrete_logarithm(7, door_public_key, 20201227)
	
assert door_loop_size != 0
assert card_loop_size != 0

encryption_key = powmod(door_public_key, card_loop_size, 20201227)
assert powmod(card_public_key, door_loop_size, 20201227) == encryption_key

print(encryption_key)