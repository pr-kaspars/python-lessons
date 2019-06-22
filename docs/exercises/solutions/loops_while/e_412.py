a = int(raw_input('Enter a number: '))
while a != 1:
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
    print(a)
