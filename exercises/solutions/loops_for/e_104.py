import math
a = int(raw_input('Enter side a: '))
b = int(raw_input('Enter side b: '))
c = int(raw_input('Enter side c: '))
p = float(a + b + c) / 2
area = math.sqrt(p * (p - a) * (p - b) * (p -c))
print(area)
