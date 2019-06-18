from math import pi
k = int(raw_input('Enter numbers: '))
x = pi / 2
sin = 0

for n in range(k + 1):
    f = 1
    for j in range(2, 2 * n + 1 + 1):
        f *= j
    sin += (pow(-1, n) * pow(x, 2 * n + 1)) / f

print('sin = ' + str(sin))
