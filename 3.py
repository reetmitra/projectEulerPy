# Problem 3

n = 600851475143
factors_prime = []
i = 2
while n >= i:
        if n % i == 0:
            factors_prime.append(i)
            n = int(n / i)
        i += 1          
print(factors_prime)