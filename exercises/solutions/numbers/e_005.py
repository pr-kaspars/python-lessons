word = raw_input('Enter a word: ')
l = len(word)
for i in range(l):
    r = ''
    for j in range(l):
        if i == 0:
            r += ' ' + word[j]
        elif i == l - 1:
            r += ' ' + word[l - j - 1]
        elif j == 0:
            r += ' ' + word[i]
        elif j == l - 1:
            r += ' ' + word[l - i - 1]
        else:
            r += '  '
    print(r)
