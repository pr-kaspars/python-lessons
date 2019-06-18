text = raw_input('Enter numbers: ')
numbers = text.split(' ')
sum = 0
for number in numbers:
    sum += float(number)

print('Mean: ' + str(sum / len(numbers)))
