from pathlib import Path
from time import ctime
from zipfile import ZipFile
import csv
import json
import sqlite3
import time
import random
import string
import webbrowser


# path = Path("ClassesPython.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# print(ctime(path.stat().st_ctime))

# ZipFile
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# CSV file write
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([2000, 2, 15])

# Read CSV file
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# JSON File
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Kindergarten cop", "year": 1990}
# ]
# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

# Read JSON file
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)

# SQLite Database commit
# movies = json.loads(Path("movies.json").read_text())
# print(movies)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# SQlite read
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "SELECT * FROM Movies"
#     cursor = conn.execute(command)
#     # for row in cursor:
#     #     print(row)
#     movies = cursor.fetchall()
#     print(movies)

# Time complexity
# def even_num():
#     even1 = []
#     for i in range(0, 500000, 2):
#         even1.append(i)
#
#     return even1
#
# def comp_even():
#     even_number = [item for item in range(500000) if item % 2 == 0]
#     return even_number
#
# def gen_even():
#     values = (x * 2 for x in range(500000))
#     value = [item for item in values]
#     return value
#
# start = time.time()
# num1 = even_num()
# end = time.time()
# duration = end - start
# print(duration)
#
# start = time.time()
# num2 = comp_even()
# end = time.time()
# duration = end - start
# print(duration)
#
# start = time.time()
# num3 = gen_even()
# end = time.time()
# duration = end - start
# print(duration)

#  Letter Count
# def letter_count(input: str):
#     count = 1
#     stored_data = ""
#     i = 0
#     j = 1
#     while i < len(input):
#         if j < len(input) and input[i] == input[j]:
#             count += 1
#         else:
#             stored_data += str(count) + input[i]
#             count = 1
#         i += 1
#         j += 1
#     print(stored_data)
#
#
# value = "aabbbddddeeeooofff"
# start = time.time()
# letter_count(value)
# end = time.time()
# duration = end - start
# print(duration)
#
#
#
#
# def word_count(string_input: str):
#     final_string = ""
#     i = 0
#     while i < len(string_input):
#         count = 1
#
#         for j in range(i + 1, len(string_input)):
#
#             if string_input[i] == string_input[j]:
#                 count += 1
#             else:
#                 break
#
#         final_string += str(count) + string_input[i]
#         i += count
#
#     print(final_string)
#
# start = time.time()
# word_count(value)
# end = time.time()
# duration = end - start
# print(duration)

# Random generate
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# Opening browser
# print("Deployment completed")
# webbrowser.open("http://google.com")