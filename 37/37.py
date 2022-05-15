import re
import sys


class Customer:
    def __init__(self, name, phone, surname, email):
        self.name = name
        self.phone = phone
        self.surname = surname
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.email} - {self.phone}"


class CustomerStorage:
    list_customers = []

    def addCustomer(self, name, surname, email, phone):
        self.list_customers.append(Customer(name, phone, surname, email))
        return str(self.list_customers[len(self.list_customers) - 1])

    def listCustomers(self):
        return self.list_customers

    def removeCustomer(self, name, surname):
        for i in range(len(self.list_customers)):
            if self.list_customers[i].name == name and self.list_customers[i].surname == surname:
                return str(self.list_customers.pop(i))

        return None

    def getCustomer(self, name, surname):
        for i in range(len(self.list_customers)):
            if self.list_customers[i].name == name and self.list_customers[i].surname == surname:
                return str(self.list_customers[i])
        return None

    def getCount(self):
        return len(self.list_customers)


def validation_name_surname(text):
    if re.search(r'[^a-zA-Zа-яА-Я]', text):
        return False
    else:
        return True


def validation_number(number):
    pattern = r'^((\+7|7|8)+([0-9]){10})$'
    return True if re.fullmatch(pattern, str(number)) is not None else False


def validation_email(email):
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    return True if re.fullmatch(pattern, email) is not None else False


customer_storage = CustomerStorage()


def execute(line):
    data = line.split()
    if len(data) == 1:
        if data[0] == 'LIST':
            list_customers = customer_storage.listCustomers()
            for customer in list_customers:
                print(customer)

        if data[0] == 'COUNT':
            print(customer_storage.getCount())

    elif len(data) == 3:
        if data[0] == 'GET':
            print(customer_storage.getCustomer(data[1], data[2]))
        elif data[0] == 'REMOVE':
            print(customer_storage.removeCustomer(data[1], data[2]))
    elif len(data) == 5 and validation_name_surname(data[1]) and validation_name_surname(data[2]) and validation_email(
            data[3]) and validation_number(data[4]):
        if data[0] == 'ADD':
            print(customer_storage.addCustomer(data[1], data[2], data[3], data[4]))
    elif len(data) == 5:
        print(None)


for line in sys.stdin:
    execute(line)
