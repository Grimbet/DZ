"""   Декоратор """
def is_prime(func):
	def wrapper(a,b,c):
		result = func(a,b,c)
		message = "Это простое число"
		if result <= 1: 
			message = "Это не простое и не составное число"
		for i in range(2, int(result**0.5) + 1): 
			if result % i == 0: 
				message="Это составное число"
		otvet = str(result) +" : "+ message		
		return otvet
	return wrapper


@is_prime
def sum_three(a,b,c):
	sum=a+b+c
	return sum

print(sum_three(0,1,0))
print(sum_three(2,1,4))
print(sum_three(2,3,3))