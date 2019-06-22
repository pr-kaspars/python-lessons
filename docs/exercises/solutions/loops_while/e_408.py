n = int(raw_input('Enter a number: '))
s, d = 0, 1
while d <= n:
    d = d * 10
    s = s + (n % d) / (d / 10)
print('Sum of digits: ' + str(s))
