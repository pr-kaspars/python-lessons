n = int(raw_input('Enter numbers: '))
factorial = 1

for i in range(2, n + 1):
    factorial = factorial * i

print('n!=' + str(factorial))
