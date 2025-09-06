# 6.
# names = ["Dima", "Yaroslav", "Zhenya", "Sasha", "Andrii", "Max"]
# for name in names:
#   print(f"Hello {name}!")

# 7-8.
# word = input("Enter word: ")
# letter_find = input("Enter letter to want find: ")
# count = 0

# for letter in word:
#   if letter == letter_find:
#     count += 1

# print(f"Wowd '{word}' has {count} letter '{letter_find}'.")

# 12.
# price_per_kg = float(input("Enter price per kg: "))
# weight = 1200
# while weight <= 2000:
#  cost = weight * price_per_kg
#  weight += 200
#  print(f"Cost {weight/1000} kg candy: {cost/1000} UAH")

# 13.
# num_sum = 0
# for num in range(0,101):
#     if num % 2 != 0:
#         num_sum += num
# print(num_sum)

# 14.
# s = int(input("Start: "))

# e = int(input("End: "))

# print("Odd numbers:")
# for number in range(s, e + 1):
#     if number % 2 != 0:
#         print(number)

# print("0")

# 15.
# def f(x):
#     if type(x) != int:
#         raise TypeError('Enter integer')
#     if x < 0:
#         raise ValueError("Enter positive integer")
#     result = 1
#     a = 1
#     if x in [0, 1]:
#         return result
#     while  a <= x:
#         result *= a
#         a += 1

#     print(result)
# f(3)

# 16
# a = int(input("(a): "))
# b = int(input("(b): "))
# c = int(input("(c): "))


# if c == 0:
#     print("c != 0")
# else:

#     if a > b:
#         a, b = b, a

#     count = 0

#     for num in range(a, b + 1):

#         if num % c == 0:
#             count += 1

#     print(f"The number of numbers between {a} and {b} that are divisible by {c} is: {count}")

