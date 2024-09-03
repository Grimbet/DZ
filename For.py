numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for i in range(len(numbers)) :
    n = numbers[i]
    tip = True
    if n <= 1:
        tip=False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            tip=False
        break
    if n != 1 :
        if tip==False :
            not_primes.append(n)
        else :
            primes.append(n)
print("Primes:     ",primes)
print("Not Primes: ",not_primes)
