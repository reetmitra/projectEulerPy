# Problem 2

target = 4000000
sum = 0
current_fib = 1
prev_fib = 1

while current_fib <= target:
    if current_fib == 1:
        current_fib += current_fib
    else:
        temp = current_fib
        current_fib += prev_fib
        prev_fib = temp

    if current_fib % 2 == 0:
        sum += current_fib

print(sum)