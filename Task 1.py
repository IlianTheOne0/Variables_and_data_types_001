a = float(input('First number: '))
b = float(input('Second number: '))
c = float(input('Third number: '))

a = int(a) if a.is_integer() else float(a)
b = int(b) if b.is_integer() else float(b)
c = int(c) if c.is_integer() else float(c)

print('Sum:', a+b+c, 'Product:', a*b*c)