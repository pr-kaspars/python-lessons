from math import factorial, pow

n = x = float(raw_input('Enter x: '))
i, sum = 0, 0
while abs(n) >= x/1000:
    n = pow(-1, i) * pow(x, 2 * i + 1) / factorial(2 * i + 1)
    sum += n
    i += 1
print(sum)
