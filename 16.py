# Problem 16

two_p = 2 ** 1000
string_two_p = str(two_p)
sum = 0 
array1 = []
newarray = []

for num in string_two_p:
    array1.append(num)

for i in array1:
    newarray.append(int(i))

for j in newarray:
    sum += j 

print(sum)