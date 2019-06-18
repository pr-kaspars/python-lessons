n = int(raw_input('Enter numbers: '))
sum = 0

for i in range(1, n + 1):
    sum += pow(-1, i + 1) * pow(i, 2)

print('sum = ' + str(sum))
