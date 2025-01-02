import math
def is_prime(n: int) -> bool:
	if  n<=1:
		return False
	if n==2 or n==3:
		return True

	if n%2==0 or n%3==0:
		return False

	i = 5
	
	while i <= math.sqrt(n):
		if n%i==0 or n%(i+2)==0:
			return False
		i+=6
	return True



print(is_prime(224))
