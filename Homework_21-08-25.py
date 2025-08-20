# for i in range(1001):
#     print(str.rjust(str(i),4,'0'))


print("Enter 'q', 'exit' or 'quit' to quit ")
while True:
    a = input('Enter your name: ')

    if a.lower().strip() in ['q', 'exit', 'quit'] :
        print('Quit...')
        break
    elif a.strip() == '':
        print("Name can't be blank")
    else:
        print(f'Hi {a}')
        print('Quit...')
        break
    