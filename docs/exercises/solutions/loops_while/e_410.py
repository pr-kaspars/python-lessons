n = int(raw_input('Enter a number: '))
d, x = 1, None
while d <= n and x != 5:
    d = d * 10
    x = (n % d) / (d / 10)
print('Contains 5: ' + str(x == 5))
