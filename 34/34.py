import sys
import re


def is_number(number):
    pattern = '^((\+7|7|8)+([0-9]){10})$'
    return True if re.fullmatch(pattern, str(number)) is not None else False


class Contacts:
    name_telephone = {}

    def add(self, name, telephone):
        if name in self.name_telephone:
            if telephone not in self.name_telephone[name]:
                self.name_telephone[name].append(telephone)
        else:
            self.name_telephone[name] = [telephone]
        print(name, ': ', ', '.join(self.name_telephone[name]), sep='')

    def find_name(self, name):
        if name in self.name_telephone.keys():  # info - имя
            print(name, ': ', ', '.join(self.name_telephone[name]), sep='')
        else:
            print(None)

    def find_telephone(self, telephone):
        exist = False
        for key in self.name_telephone.keys():
            if telephone in self.name_telephone[key]:
                exist = True
                print(key, ': ', ', '.join(self.name_telephone[key]), sep='')
                break
        if not exist:
            print(None)

    def print(self):
        for key in sorted(self.name_telephone.copy().keys()):
            print(key, ': ', ', '.join(self.name_telephone[key]), sep='')


contacts = Contacts()


def execute(command):
    data = command.split()
    if len(data) == 2:
        if is_number(data[1]) or is_number(data[0]):
            if is_number(data[1]):
                number = data[1]
                name = data[0]
            else:
                number = data[0]
                name = data[1]
            if re.search(r'[^a-zA-Zа-яА-Я]', name[0]):
                pass
            else:
                contacts.add(name, number)

    if len(data) == 1:
        if data[0] == 'LIST':
            contacts.print()
        elif is_number(data[0]):
            contacts.find_telephone(data[0])
        else:
            if re.search(r'[^a-zA-Zа-яА-Я]', data[0][0]):
                pass
            else:
                contacts.find_name(data[0][0])


for line in sys.stdin:
    execute(line)
