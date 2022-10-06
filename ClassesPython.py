from abc import ABC, abstractmethod


# class Point:
#     def draw(self):
#         print("Draw")

# Construction
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def zero(cls):
#         return cls(0, 0)
#
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# class TagCLoud:
#     def __init__(self):
#         self.tags = {}
#
#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
#
#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)
#
#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count
#
#     def __len__(self):
#         return len(self.tags)
#
#     def __iter__(self):
#         return iter(self.tags)

# class Product:
#     def __init__(self, price):
#         self.price = price
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be Negative")
#         self.__price = value


# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1
#
#     def eat(self):
#         print("Eat")
#
#
# class Mammal(Animal):
#     def __init__(self):
#         print("Mammal Constructor")
#         self.weight = 2
#         super().__init__()
#
#     def walk(self):
#         print("Walk")


# class InvalidOperatorError(Exception):
#     pass
#
#
# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
#
#     def open(self):
#         if self.opened:
#             raise InvalidOperatorError("Stream is already open")
#         self.opened = True
#
#     def close(self):
#         if not self.opened:
#             raise InvalidOperatorError("Stream is already Close")
#         self.opened = False
#
#     @abstractmethod
#     def read(self):
#         pass
#
#
# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")
#
#
# class NetworkStream(Stream):
#     def read(self):
#         print("Reaading data from network")
#
#
# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream")


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class Textbox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Drop DownList")


def draw(controls):
    for control in controls:
        control.draw()


if __name__ == '__main__':
    # Polymorphism
    ddl = DropDownList()
    textbox = Textbox()
    draw([ddl, textbox])

    # Another Example of Inheritence
    # stream = MemoryStream()
    # stream.open()

    # Method Overriding
    # m = Mammal()
    # print(m.walk)
    # print(m.eat)
    # print(m.weight)
    # print(m.age)

    # Properties
    # product = Product(10)
    # product.price = 20
    # print(product.price)

    # cloud = TagCLoud()
    # cloud["Python"] = 10
    # print(len(cloud))
    # cloud.add("Python")
    # cloud.add("Python")
    # cloud.add("Python")
    # print(cloud.tags)

    #   Initializing construction
    # point = Point(1, 2)
    # point.draw()
    # point = Point.zero()
    # point.draw()

    # Create Class
    # point = Point()
    # print(type(point))
    # print(isinstance(point, Point))
