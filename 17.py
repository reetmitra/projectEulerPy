# Problem 17 

dictionary1 = {n:0 for n in range(0,1001)}

dictionary1[0] = 0
dictionary1[1] = 3
dictionary1[2] = 3
dictionary1[3] = 5
dictionary1[4] = 4
dictionary1[5] = 4
dictionary1[6] = 3
dictionary1[7] = 5
dictionary1[8] = 5
dictionary1[9] = 4
dictionary1[10] = 3
dictionary1[11] = 6
dictionary1[12] = 6
dictionary1[13] = 8
dictionary1[14] = 8
dictionary1[15] = 7
dictionary1[16] = 7
dictionary1[17] = 9
dictionary1[18] = 8
dictionary1[19] = 8
dictionary1[20] = 6
dictionary1[30] = 6
dictionary1[40] = 5
dictionary1[50] = 5
dictionary1[60] = 5
dictionary1[70] = 7
dictionary1[80] = 6
dictionary1[90] = 6

for i in range(21,100):
    tens = int(i/10)*10
    ones = i - tens
    dictionary1[i] = dictionary1[tens] + dictionary1[ones]

for i in range(100,1000):
    hundreds = int(i/100)
    tens_ones = i - hundreds*100

    if tens_ones == 0:
        dictionary1[i] = dictionary1[hundreds] + 7
    else:
        dictionary1[i] = dictionary1[hundreds] + 10 + dictionary1[tens_ones]

dictionary1[1000] = 11

print(sum(dictionary1.values()))
