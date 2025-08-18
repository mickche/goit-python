v1 = 'Variable'
v2 = 1
v3 = 2.32
v4 = True
v5 = ['1',2,False]
v6 = (13,45.78)
v7 = {
    '1':2,
    '2':3
}

# print(type(v1))
# print(type(v2))
# print(type(v3))
# print(type(v4))
# print(type(v5))
# print(type(v6))
# print(type(v7))

# print(f'Довжина v1:{len(v1)}')
# print(f'Довжина v5:{len(v5)}')
# print(f'Довжина v6:{len(v6)}')
# print(f'Довжина v7:{len(v7)}')

# print(f'Id v1:{id(v1)}')
# print(f'Id v2:{id(v2)}')
# print(f'Id v3:{id(v3)}')
# print(f'Id v4:{id(v4)}')
# print(f'Id v5:{id(v5)}')
# print(f'Id v6:{id(v6)}')
# print(f'Id v7:{id(v7)}')











# number = 1024

# print(f'{len(bin(number))-2}')

# def int_to_list(x:int)-> list:
#     my_list = []
#     while x:
#         x,y = divmod(x,10)
#         my_list.append(y)
#     return my_list

# my_list = int_to_list(x=number)
# print(f'Число {number} має довжину {len(my_list)}')



# def v(x):
#     if type(x) == str:
#         print("Ви ввели str")
#     elif type(x) == int:
#         print("Ви ввели int")
#     else:
#         print(f'Ви ввели {type(x).__name__}')
#         # print(type(x).__name__)
# v(1.45)


# def triangle(stars_number=7, alignment='left', flipped=False):
#     if alignment == 'left':
#         align_func = str.ljust
#     elif alignment == 'right':
#         align_func = str.rjust
#     else:
#         raise ValueError("Unknown alignment")
#     lines = [
#         align_func(('*' * (i+1)), stars_number)
#         for i in range(stars_number)
#     ]
#     if flipped:
#         print(*(reversed(lines)), sep='\n')
#     else:
#         print(*lines, sep='\n')
#     print()
# try:
#     triangle(stars_number=10, alignment='left', flipped=True)
# except ValueError as e:
#     print(e, ":\tUse 'left' or 'right'")

# def triangle(stars_number=7):
#     for i in range(stars_number):
#        stars = i+1
#        print('*'* stars)

# triangle()
# print()

# def flipped_triangle(stars_number=7):
#      for i in range(stars_number):
#         stars = stars_number - i
#         print( '*'* stars )
# flipped_triangle()