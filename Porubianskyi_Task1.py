print('Мультипарадигмальні мови програмування. Лабороторна робота №1')
print('Порубянський Валентин Валентинович, Група ІКМ-221д ')

#use "if"
name = 'Владислав Валерійович'
count = 45
long_name2 = ''
for i in range(count):
    if i < count-1:
        long_name2 += name + ", "
    else:
        long_name2 += name
print(long_name2)

# use "*"
name = 'Владислав Валерійович'
long_name3 = (name + ', ') * 44 + name
print(long_name3)

# variant 12
result = (176-9.3/7)/(18.2-179.3)-323.8**2
print(round(result, 2))

