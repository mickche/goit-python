# a = 0
# for x in range(7):
#     a += x

# print(a)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="\t")

a = int(input())
b = int(input())
c = int(input())
d = int(input())


#print header
print(end = '\t')
for i in range(c, d + 1) :
    print(i, end = '\t')
print("")

#print table
for i in range(a, b + 1) :
    print(i, end = '\t')
    for j in range(c, d + 1) :
        print(i * j, end = '\t')
    print("")

# while False:
#     print('Hi')
# else:
#     print('Bye')



# a = int(input())
# b = int(input())


# sum = 0
# count = 0


# for i in range(a, b + 1) :
#     if (i % 3) == 0 :
#         sum += i
#         count += 1


# print(sum / count)

# while True:
#     i = int(input())

#     if i > 100 :
#         break

#     if i < 20 :
#         continue

#     print(i)

# while True:
#     number = input("number = ")
#     number = int(number)
#     while True:
#         print(number)
#         number = number - 1
#         if number < 0:
#             break