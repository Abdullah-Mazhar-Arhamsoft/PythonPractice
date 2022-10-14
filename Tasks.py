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
