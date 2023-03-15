""" Multi-paradigm movie programming.
Laboratory work №1.
Porubyanskiy Valentin, Group IKM-221d """

print('Multi-paradigm movie programming.Laboratory work №1')
print('Porubyanskiy Valentin, Group IKM-221d ')


def validate_input(var_name):
    while True:
        try:
            return int(input('Add value for variable {}:'.format(var_name)))
        except ValueError:
            print('Enter please correct value (number)')


x = validate_input('x')
y = validate_input('y')
z = validate_input('z')

result = (176 - y / 7) / (18.2 + x) - 23.8 ** z
print('(176 - y / 7) / (18.2 + x) - 23.8 ** z =', round(result, 2))
