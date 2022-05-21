# Problem 6

sum = 0
sum_two = 0

for i in range(1,101):
    sum += i**2
print(sum)

for i in range(1,101):
    sum_two += i
sum_two = sum_two ** 2
print(sum_two)

difference = sum_two - sum
print(f"The difference is: {difference}")