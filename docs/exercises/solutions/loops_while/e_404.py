n = int(raw_input('Enter a number: '))
i = 0
p, c = 0, 1
while c < n:
    t = c
    c, p, i = p + c, t, i + 1

if c is n:
    print('Index in Fibonacci sequence: ' + str(i))
else:
    print('The number is not in Fibonacci sequence')
