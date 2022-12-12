# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def increment(number: int, by: int) -> tuple:
#     return (number, number + by)
#
#
# def multiply(*user_list):
#     total = 1
#     for number in user_list:
#         total *= number
#     return total
#
#
# def save_user(**user):
#     print(user)
#     print(user["name"])


# def fizz_buzz(num: int) -> None:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# def calculate_xfactor(age) :
#     if age <= 0:
#         raise ValueError("Age cannot be less or zero")
#     return 10/age


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # hello


    # try:
    #     calculate_xfactor()
    # except ValueError as error:
    #     print(error)

    # Exception Handling
    # try:
    #     with open("main.py") as file:
    #         print("File opened")
    #             # OR
    #     file = open("main.py")
    #     age = int(input("Age: "))
    #     xfactor = 10 / age
    # except (ValueError, ZeroDivisionError) as ex:
    #     print("You didn't enter a valid age")
    #     print(ex)
    #     print(type(ex))
    # else:
    #     print("No exception were thrown")
    # finally:
    #     file.close()
    # print("Execution continues")

    # Most count letter
    # Optimized way
    # sentence = 'This is a common interview question'
    #
    # stored_data = {}
    # for data in sentence:
    #     if data in stored_data:
    #         stored_data[data] += 1
    #     else:
    #         stored_data[data] = 1
    # print(dict(sorted(stored_data.items(), key=lambda x: x[1], reverse=True)))00.0

    # less Optimized way
    # sentence_list = [*sentence.lower()]
    # sentence_list.sort()
    # joined = "".join(sentence_list)
    # sentence_list = [*joined.strip()]
    # print(sentence_list)
    # i = 0
    # count = 1
    # stored = {}
    # while i < (len(sentence_list) - 1):
    #     if sentence_list[i] == sentence_list[i + 1]:
    #         count += 1
    #         stored[sentence_list[i]] = count
    #         i += 1
    #     # elif i == (len(sentence_list)-2):
    #     #     pick = {sentence_list[i+1]: count}
    #     #     stored.update(pick)
    #     else:
    #         stored[sentence_list[i]] = count
    #         count = 1
    #         i += 1
    # print(stored)
    # max_value = max(stored.values())
    # max_key = max(stored, key=stored.get)
    # print("Letter: ", max_key)
    # print("Count: ", max_value)
    # for x in sentence_list :
    #     if x[i] == x[i+1] :
    #         count = count + 1
    #         stored = {x[i]: count}
    #         i += 1
    #     else:
    #         break

    # Comprehension
    # items = [
    #     ("Product1", "ok", 10),
    #     ("Product2", "ok", 9),
    #     ("Product3", "ok", 12),
    # ]
    # prices = [item[2] for item in items]
    # print(prices)
    # filtered = [item for item in items if item[2] >= 10]
    # print(filtered)

    # filtered and mapped
    # items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # filtered = list(filter(lambda item: item % 2 == 0, items))
    # print(filtered)
    # mapped = list(map(lambda item: item % 2 == 0, items))
    # print(mapped)

    # Sort items with lambda func and mapping
    # items = [
    #     ("Product1", "ok", 10),
    #     ("Product2", "ok", 9),
    #     ("Product3", "ok", 12),
    # ]
    # # items.sort(key=lambda item: item[2])
    # # print(items)
    # prices = list(map(lambda item: item[2], items))
    # prices.sort()
    # print(prices)

    # Looping over List
    # letters = [('a', 'l'), ('b', 'm'), ('c', 'n'), ('d', 'o')]
    # for index, letter in enumerate(letters):
    #     print(index, letter)

    # Filter Method
    # items = [
    #     ("Product1", "ok", 10),
    #     ("Product2", "ok", 9),
    #     ("Product3", "ok", 12),
    # ]
    #
    # filtered = list(filter(lambda item: item[2] >= 10, items))
    # print(filtered)

    # Chap 2 exercise
    # fizz_buzz(0)

    # **args
    # save_user(id=1, name='admin')

    # Split Email
    # email = "nouman.arhamsoft@gmail.co.net"
    # email_split = email.find('@')
    # domain_split = email.find('.')
    # main_domain_split = email.find('.', domain_split + 1)
    # username = email[:email_split]
    # sub_domain = email[email_split + 1:main_domain_split]
    # main_domain = email[main_domain_split+1:]
    # print('Username: ', username)
    # print('Sub Domain: ', sub_domain)
    # print('Main Domain: ', main_domain)

    # email_split = email.split("@")
    # username = email_split[0]
    # domain = email_split[1].split(".")
    # sub_domain = domain[0]
    # main_domain = domain[1]
    # print("Username: ", username)
    # print("Sub Domain: ", sub_domain)
    # print("Main Domain: ", main_domain)

    # print(increment(2, 5))
    # print(multiply(2, 3, 4, 5))

    # While Loop
    # guess = 0
    # answer = 5
    # while answer != guess:
    #     guess = int(input("Guess: "))
    #     if answer == guess :
    #         print("Found")

    # For-else loop
    # names = ["John", "Mary"]
    # for name in names:
    #     if name.startswith("M"):
    #         print("Found")
    #         break
    # else:
    #     print("Not Found")

    # Ternary operators
    # age = 22
    # message = "ok" if age >= 18 else "not ok"
    # print(message)

    # numbers
    # b = 5
    # k = 6
    # c = complex(b,k)
    # print(c)
    # print(list(range(10)))
    # print(list(range(2,12,2)))
    # x = 4.1
    # print(math.ceil(x))
    # print(math.copysign(2.0, -1.0))

    # Find method.
    # name2 = "python is propramming"
    # name1 = "Helllllllllllllllllllllooooooooooooooooo"
    # index_of_l = name1.find('l', name1.find('l', name1.find('l') + 1) + 1)
    # index_of_p = name2.find('p', name2.find('p', name2.find('p') + 1) + 1)
    # print(index_of_l)
    # print(name1[:index_of_l] + 'o')
    # print(name1[:4] + 'o')

