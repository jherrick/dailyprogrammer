def gcd(a, b):
	while b: 
		a, b = b, a%b
	return a

def fractions(x, y):
	return x / gcd(x,y), y / gcd(x,y) 

print fractions(1536, 78360)