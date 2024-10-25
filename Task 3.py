a = float(input('First diagonal: '))
b = float(input('Second diagonal: '))

result = (1/2)*a*b

if result.is_integer():
    result = int(result)

print('Result:', result)