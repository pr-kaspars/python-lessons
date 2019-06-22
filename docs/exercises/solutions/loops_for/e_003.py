r = int(raw_input('Enter r: '))
n = int(raw_input('Enter n: '))
for i in range(r):
    row = ''
    for j in range(n):
        row = row + '*'
    print(row)
