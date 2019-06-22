n = int(raw_input('Enter a number: '))
d, i = 1, 0
while d <= n:
    d = d * 10
    if (n % d) / (d / 10) == 5:
        i += 1
print('Count: ' + str(i))
