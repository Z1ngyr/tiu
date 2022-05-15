import sys


class TodoList:
    todo_list = []

    def add(self, name):
        self.todo_list.append(name)

    def add_with_index(self, name, index):
        self.todo_list.insert(index - 1, name)

    def edit(self, name, index):
        self.todo_list[index - 1] = name

    def delete(self, index):
        self.todo_list.pop(index - 1)

    def print(self):
        for i in range(len(self.todo_list)):
            print(str(i + 1), self.todo_list[i], sep=' - ')


todolist = TodoList()


def execute(command):
    data = command.split()
    if data[0] == 'ADD':
        if len(data) == 2:
            todolist.add(data[1])
        elif len(data) == 3:
            todolist.add_with_index(name=data[2], index=int(data[1]))
    elif data[0] == 'EDIT':
        if int(data[1]) - 1 <= len(todolist.todo_list) and int(data[1]) > 0:
            todolist.edit(data[2], int(data[1]))
    elif data[0] == 'DELETE':
        if int(data[1]) - 1 < len(todolist.todo_list) and int(data[1]) > 0:
            todolist.delete(int(data[1]))
    elif data[0] == 'LIST':
        todolist.print()


for line in sys.stdin:
    execute(line)
