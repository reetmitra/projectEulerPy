# Problem 4

record_array = []

for i in range(100,999):
    for j in range(100,999):
        num = i * j
        if (str(num) == str(num)[::-1]):
            record_array.append(num)
print(max(record_array))