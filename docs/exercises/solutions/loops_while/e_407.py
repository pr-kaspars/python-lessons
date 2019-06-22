n = int(raw_input('Enter a number: '))
i, d = 1, 10
while d <= n:
    d = d * 10
    i += 1
print('Number of digits: ' + str(i))
