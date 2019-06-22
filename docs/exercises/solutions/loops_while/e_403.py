print('2*2=?')
answer = None
guesses = 0
while answer is not 4 and guesses < 3:
    answer = int(raw_input('Answer: '))
    guesses += 1
if answer is 4 and guesses < 3:
    print('Correct!')
else:
    print('Cerrect answer is 4 :(')
