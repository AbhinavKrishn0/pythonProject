a = input('Select Operation ?')
b = int(input('> '))
c = int(input('> '))
if a == 'Addition':
    print(int(b + c))
elif a == 'Subtraction':
    print((b - c))
elif a == 'Multiplication':
    print((b * c))
elif a == 'Division':
    print((b / c))
else:
    print('Invalid Input')
