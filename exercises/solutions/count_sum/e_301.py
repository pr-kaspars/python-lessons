text = raw_input('Enter text: ')
count = 0

for l in text:
    if l == ' ':
        count += 1

if count != 0:
    count += 1

print('Words: ' + str(word_count))
