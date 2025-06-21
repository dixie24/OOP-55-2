# class Animal:
#     def make_sound(self):
#         return "издает звук"
#
#
# class Swimable:
#     def move(self):
#         return "Плавает"
#
# class Flyable:
#     def move(self):
#         return "Летит"
#
#
# class Duck(Animal, Flyable, Swimable):
#     pass
#
# donald = Duck()
# print(Duck.__mro__)
#


# class A:
#     def test_method(self):
#         return "Class A"
#
# class B(A):
#     def test_method(self):
#         return super().test_method()
#         # return "Class B"
#
# class C(A):
#     def test_method(self):
#         return super().test_method()
#
# class D(B,C):
#     pass
#     # def test_method(self):
#     #     return "Class D"
#
# obj = B()
#
# print(B.__mro__)

# 1. Декоратор @staticmethod
# Описание:
# Декоратор @staticmethod используется для того, чтобы определить метод, который не зависит от экземпляра класса
# (не использует self) и не зависит от самого класса (не использует cls). Такой метод можно вызывать без создания
# экземпляра класса.

# 2. Декоратор @classmethod
# Описание:
# Декоратор @classmethod используется для определения метода, который принимает первым аргументом
# сам класс (не экземпляр). Этот аргумент обычно называется cls. Метод класса может изменять состояние класса,
#  но не работает с состоянием конкретного экземпляра.



# import logging
# class Math:
#     # Атрибут класса
#     sum = print("123")
#
#     def __init__(self, test):
#         # Атрибут экземпляра|объекта класса
#         self.test = test
#
#     @staticmethod
#     def add(a,b):
#         return a + b
#
#     @classmethod
#     def get_sum(cls):
#         return cls.sum
#
#     def just_method(self):
#         return None

# print(Math.sum)

# 3. Декоратор @property
# Описание:
# Декоратор @property используется для того, чтобы метод стал доступным как атрибут, но при этом оставался методом.
# Это позволяет скрывать логику вычислений или проверки, делая код более чистым. Обычно используется
# для создания геттеров и сеттеров.

# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     @property
#     def get_radius(self):
#         return self.__radius
#
#     @property
#     def area(self):
#         return 3.14 * self.__radius
#
#
# circle = Circle(5)
# #
# print(circle.get_radius)
#
# Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию в качестве аргумента и возвращает
# измененную или новую функцию. Они позволяют добавлять новую функциональность к существующим
# функциям без изменения их кода.

#                 def hello() 1 step
# def my_decorator(func):
#
#     def wrapper(): #step 2
#         print('Перед выполнением функции') # step 3
#         func()  # step 4
#         print('После выполнения функции') # step 5
#     return wrapper # step 6
#
# @my_decorator
# def hello():
#     print('hello world!!')
#
# @my_decorator
# def test():
#     print("test")

# hello()
# test()

# def test(a,b)
# test(12,32)

# Декораторы с параметрами|аргументы
#          5

# def repeat(n):
#     #             def hello()
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator
#
# @repeat(5)
# def hello():
#     print("Hello")

# hello()


# def class_decorator(cls):
#
#     class NewClass(cls):
#         def new_method(self):
#             return "Новый метод!!!"
#
#     return NewClass
#
# @class_decorator
# class MyClass:
#     def old_method(self):
#         return "Старый метод"
#
# obj = MyClass()
#
# print(obj)


# class A:
#     def a(self):
#         return 'a'
#
# class B(A):
#     def b(self):
#         return "b"
#
# class C(A):
#     def b(self):
#         return "b"