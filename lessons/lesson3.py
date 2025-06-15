# Инкапсуляция
from tokenize import blank_re


class BankAccount:

    def __init__(self, user_name, balance, password):
        self.user_name
        self._balance = balance
        self.password = password



jim = BankAccount("jim", 1000, 000)

print(jim._balance)

from abc import ABC, abstractmethod

class Animal(ABC):

    @