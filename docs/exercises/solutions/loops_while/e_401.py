count = 0
sum = 0.0
number = None
while number is not 0:
    number = int(raw_input('Enter a number: '))
    sum += number
    count += 1
print(sum / count)
