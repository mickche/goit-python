# a = input("Введіть своє ім'я: ")
# print(f'Привіт {a}')

# b = int(input('Enter number: '))
# print(f'Your number: {b}')

# a,b,c, = input('Enter some text: ').split(' ')
# print(a,b,c)

print('Enter q to quit ')
while True:
    a = input('Enter your name: ')
    d = a.split()
    if  'q' in d or 'q' in d[0] or 'q' in d[-1]:
        b = d[0]
        print(f'Hi {b}')
        print('Quit...')
        break

    elif a == '' or a ==  ' ':
        print('\n')

    print(f'Hi {a}')

