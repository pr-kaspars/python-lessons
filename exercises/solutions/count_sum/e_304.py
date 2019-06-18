text = raw_input('Enter numbers: ')
positive = 0
negative = 0

for number_str in text.split(' '):
    number = int(number_str)
    if number > 0:
        positive += 1
    elif  number < 0:
        negative += 1

print('Positive: ' + str(positive))
print('Negative: ' + str(negative))
