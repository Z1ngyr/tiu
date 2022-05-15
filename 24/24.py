import random


def generatePatietsTemperatures(n):
    random.seed(1234)
    for i in range(n):
        yield round(random.uniform(30, 42), 1)


def getReport(n):
    arr = []
    count = 0
    for temp in generatePatietsTemperatures(n):
        arr.append(temp)
        if 35.5 <= temp <= 37:
            count += 1
    average = round(sum(arr) / len(arr), 1)
    return arr, average, count


arr, average, count = getReport(int(input()))
print(*arr, sep=', ')
print(average)
print(count)
