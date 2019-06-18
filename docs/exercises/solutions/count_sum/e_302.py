text = raw_input('Enter text: ')
count = 0

for i in range(len(text) - 1):
    if text[i] + text[i + 1] == 'th':
        count += 1

print('Count: ' + str(count))
