# Problem 7 

def IsPrime(n):
    if (n > 1):
        for i in range(2, n - 1):
            if(n % i == 0):
                return False
        return True 
    return False

n = 0
count = 0

while count < 10001:
    n += 1
    if(IsPrime(n)):
        count += 1    

print(n)