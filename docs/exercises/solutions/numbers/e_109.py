mm_in = int(raw_input('Enter a number: '))
m = (mm_in - (mm_in % 1000)) / 1000
cm = (mm_in - m * 1000) / 10
mm = mm_in - m * 1000 - cm * 10
print('{}mm = {}m {}cm {}mm'.format(mm_in, m, cm, mm))
