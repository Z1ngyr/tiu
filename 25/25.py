# так как в этой задаче ввод точек ничем не ограничен, приходится использоваться sys.stdin
# для его полной симуляции создается отдельный файл и настраивается input из этого файла
# когда будете код прикладывать надо только этот код скинуть)
# кста поаккуратней с пробелами в метода __str__
# на скрине не совсем ясно как они расставлены если что поменяете на ходу за 2 секунды
from math import *
import sys


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def length(self, other):
        return round(sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2), 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.startX = float(start.x)
        self.startY = float(start.y)
        self.endX = float(end.x)
        self.endY = float(end.y)

    def length(self):
        return Point.length(self.start, self.end)

    def __str__(self):
        return f"[{self.startX, self.startY} {self.endX, self.endY}]"


class Polyline:
    def __init__(self):
        self.segments = []

    def add_segment(self, line):
        self.segments.append(line)

    def length(self):
        sum = 0
        for line in self.segments:
            sum += Line.length(line)
        return round(sum, 2)

    def __str__(self):
        return ' - '.join([str(el) for el in self.segments])


arr_points = []
for line in sys.stdin:
    coordinates = line.split()
    arr_points.append(Point(int(coordinates[0]), int(coordinates[1])))

print(arr_points[0])  # 1 точка
print(Point.length(arr_points[1], arr_points[2]))  # расстояние между двумя точками
line_P1P2 = Line(arr_points[0], arr_points[1])
print(line_P1P2)  # Линия P1 P2
print(line_P1P2.length())
polyline = Polyline()
for i in range(len(arr_points) - 1):
    polyline.add_segment(Line(arr_points[i], arr_points[i + 1]))
print(polyline)  # Полилиния
print(polyline.length())  # Длина полилинии
