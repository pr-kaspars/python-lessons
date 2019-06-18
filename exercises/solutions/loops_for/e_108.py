x = float(raw_input('Enter a number: '))
d = int(x * 100) % 10
n = int(x * 100) - d + (10 if d > 4 else 0)
print(n / 100.0)
