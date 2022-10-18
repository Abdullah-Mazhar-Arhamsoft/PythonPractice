import time
import re

# Task 1
# x = ['is67', 'be3st', 'f23or', 'ge9eks', 'is67']
# start = time.time()
# print(sorted(x, key=lambda v: int(re.findall(r"\d+", v)[0])))
# end = time.time()
# print(end - start)
#
# l = [ 'is67', 'be3st', 'f23or', 'ge9eks', 'is67']
# start = time.time()
# print(sorted(l, key=lambda x: int("".join([i for i in x if i.isdigit()]))))
# end = time.time()
# print(end - start)

# Task 2
# numbers = range(10)
# previous_num = 0
# for i in numbers:
#     sum = previous_num + i
#     print('Current number: ', i, ' Previous number: ', previous_num, 'sum: ', sum)
#     previous_num = i

# Task 3
# str = input('Enter Word: ')
# i = 0
# size = len(str)
# while i < size:
#     print(str[i])
#     i = i + 2
#
# for x in range(0, size - 1, 2):
#     print(str[x])
#
# z = list(str)
# for x in z[0::2]:
#     print(x)

# Task 4
# def remove_word(word, n):
#     print(word[n:])
#
# str =str(input('Enter word here: '))
# number = int(input("Enter number here: "))
# remove_word(str, number)

# Task 5
# def Check_numbers(user_list):
#     print( f"Result: {user_list[0] == user_list[-1]}")
#
#
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# Check_numbers(numbers_x)
# Check_numbers(numbers_y)

# Task 6
# str_x = "Emma is good developer. Emma is a writer"
# str_split = str_x.split()
# count = 0
# for x in str_split:
#     if x == 'Emma':
#         count += 1
#
# print('Emma appeared', count, 'times.')
# print(str_x.count('Emma'))

# Task 7
# for i in range(1, 6):
#     for j in range(0, i):
#         print(i, end=" ")
#     print()
#
# k = 1
# for i in range(1, 6):
#     for j in range(0, i):
#         print(k, end=" ")
#         k += 1
#     print()

# for i in range(1, 6):
#     for j in range(1, 6):
#         if abs(i - j) == 2 or i % 2 == 0 and i - j == 0:
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1, 4):
#         if i == 1 or i == 3:
#             print('*', end=" ")
#         elif abs(i - j) == 1 or abs(i - j) == 3 or abs(i - j) == 4 or abs(i - j) == 2:
#             if i == 4 and abs(i - j) == 2 or i == 5 and abs(i - j) == 3:
#                 print(' ', end=" ")
#             else:
#                 print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, 4):
#         if j == 1 or j == 3:
#             print('*', end=" ")
#         elif abs(i - j) == 1:
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

# print()


# Printing Your name
# n = int(input('Enter size : '))
#
# while n < 8:
#     print("Size lesser than 8. Try again")
#     n = int(input('Enter size : '))
#
# last = (n//2)-1
#
# # Letter A
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or j == last or (i == 0 or i == last):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter B
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or (j == last and i != 0 and i != last and i != n-1) or ((i == 0 or i == last or i == n-1) and j != last):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
# # Letter D
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or (j == last and i != 0 and i != n-1) or ((i == 0 or i == n-1) and j != last):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter U
# for i in range(n):
#     for j in range(n // 2):
#         if ((j == 0 or j == last) and i != n-1) or (i == n-1 and (j != 0 or j != last)):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter L
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or i == n-1 :
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter L
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or i == n-1 :
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter A
# for i in range(n):
#     for j in range(n // 2):
#         if j == 0 or j == last or (i == 0 or i == last):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()
#
# print()
#
# # Letter H
# for i in range(n):
#     for j in range(n // 2):
#         if (j == 0 or j == last) and i != last or (i == last and (j != 0 or j != last)):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()


# Task 8
# x = 30
# y = 20
# print('Before swaping: ')
# print('x: ', x)
# print('y', y)
#
# x = x+y
# y = x-y
# x = x-y
#
# x = x/y
# y = x*y
# x = y/x
#
# print('After swaping: ')
# print('x: ', x)
# print('y', y)