import random
def random_sum():    
	s = random.randint(3, 9)    
	a = random.randint(1, s-1)    
	b = s - a    
	return s, (a, b)
	if __name__ == '__main__':    
		print random_sum()X