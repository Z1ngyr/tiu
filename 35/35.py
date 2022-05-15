from math import *


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

    def distance_from_point(self, point):
        A = (self.startY - self.endY) / (self.startX - self.endX)
        B = -1
        C = self.endY - A * self.endX
        return round(abs(A * point.x + B * point.y + C) / sqrt(A ** 2 + B ** 2), 2)

    def is_point_on_line(self, point):
        A = (self.startY - self.endY) / (self.startX - self.endX)
        B = -1
        C = self.endY - A * self.endX
        return A * point.x + B * point.y + C == 0

    def __str__(self):
        return "{0:.2f}".format(self.endX - self.startX) + ", {0:.2f}".format(self.endY - self.startY)


arr_points = []
for i in range(4):
    data = input().split()
    x, y = data[0], data[1]
    arr_points.append(Point(x, y))
print(arr_points[0])
print(Point.length(arr_points[1], arr_points[2]))
l1 = Line(arr_points[0], arr_points[1])
print(l1)
print(l1.length())
print(l1.distance_from_point(arr_points[2]))
print(l1.is_point_on_line(arr_points[3]))
