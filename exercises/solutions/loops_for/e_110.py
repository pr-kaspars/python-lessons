s_in = int(raw_input('Enter a number: '))
h = (s_in - (s_in % 3600)) / 3600
m = (s_in - h * 3600) / 60
s = s_in - h * 3600 - m * 60
print('{}s = {}h {}m {}s'.format(s_in, h, m, s))
