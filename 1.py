# Problem 1

numArray = []
sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        numArray.append(i)
for num in numArray:
    sum += num
    num +=1
print(sum)