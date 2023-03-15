""" Multi-paradigm movie programming.
Laboratory work №1.
Porubyanskiy Valentin, Group IKM-221d """

import math as m

print('Multi-paradigm movie programming.Laboratory work №1')
print('Porubyanskiy Valentin, Group IKM-221d ')

def validate_input(var_name):
    while True:
        try:
            return int(input('Add value for variable {}:'.format(var_name)))
        except ValueError:
            print('Enter please correct value (number)')
# TODO: add check for Z != 0

x = validate_input('x')
# y = validate_input('y')
z = validate_input('z')

result = m.sqrt(m.fabs(x ** 2 - 4)) / 2 * z
print(round(result, 2))
