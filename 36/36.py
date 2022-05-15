import re
import sys


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}"


class Lion(Animal):
    def __init__(self, name, age, bodyLength):
        super().__init__(name, age)
        self.bodyLength = bodyLength

    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}, длина тела: {self.bodyLength}"


class Monkey(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color.lower()

    def __str__(self):
        return f"Имя: {self.name}, возраст: {self.age}, цвет: {self.color}"


class Zoo:
    all_animals = []
    count_lion = 0
    count_monkey = 0

    def add_animal(self, name, age):
        self.all_animals.append(Animal(name, age))

    def add_lion(self, name, age, bodyLength):
        self.all_animals.append(Lion(name, age, bodyLength))
        self.count_lion += 1

    def add_monkey(self, name, age, color):
        self.all_animals.append(Monkey(name, age, color))
        self.count_monkey += 1

    def report(self):
        print(
            f"Всего животных: {len(self.all_animals)}. Из них львов - {self.count_lion}, обезьян - {self.count_monkey}")

    def list(self):
        for i in range(len(self.all_animals)):
            print(f"{i + 1}) {self.all_animals[i]}")


our_favorite_zoo = Zoo()


def validation_name_color(text):
    if re.search(r'[^a-zA-Zа-яА-Я]', text):
        return False
    else:
        return True


def execute(line):
    data = line.split()

    if len(data) == 1:
        if data[0] == 'LIST':
            our_favorite_zoo.list()
        elif data[0] == 'REPORT':
            our_favorite_zoo.report()
    elif len(data) > 2 and data[0] == 'ADD' and validation_name_color(data[1]) and data[1][0].isupper():
        if len(data) == 3:
            our_favorite_zoo.add_animal(data[1], data[2])
        elif len(data) == 4:
            if validation_name_color(data[3]):
                our_favorite_zoo.add_monkey(data[1], data[2], data[3])
            else:
                our_favorite_zoo.add_lion(data[1], data[2], data[3])


for line in sys.stdin:
    execute(line)
