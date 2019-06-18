x = int(raw_input('Enter x: '))
for i in range(1, x / 2 + 1):
    if x % i == 0:
        print(i)
print(x)
