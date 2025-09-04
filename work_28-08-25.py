# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# if x > 0 and y > 0:
#     print('I')

# elif x < 0 and y > 0:
#     print('II')

# elif x < 0 and y < 0:
#     print('III')

# elif x > 0 and y < 0:
#     print('IV')


# x = int(input("Введи X: "))
# y = int(input("Введи Y: "))

# if x == 0 and y == 0:
#     print("Точка у початку координат")
# elif x == 0:
#     print("Точка на осі Y")
# elif y == 0:
#     print("Точка на осі X")
# else:
#     if y > 0:
#         print("Точка у І чверті" if x > 0 else "Точка у ІІ чверті")
#     else:
#         print("Точка у IV чверті" if x > 0 else "Точка у ІІІ чверті")

numbers = [int(i) for i in input('Enter num/s: ').split()]
suma = 0


for number in numbers :
    suma += number

suma /= len(numbers)

print(suma)
