def create_pascal_triangle(n):
    row = [1]
    arr = [[0] * i for i in range(1, n+1)]
    for i in range(n):
        arr[i] = row
        row = [sum(x) for x in zip([0] + row, row + [0])]
    return arr


def print_pascal_triangle(pascal_triangle):
    n = len(pascal_triangle)
    for i in range(n):
        print('_' * (n - len(pascal_triangle[i])), end='')
        for j in range(0, len(pascal_triangle[i])):
            print(pascal_triangle[i][j], end='')
            if j != len(pascal_triangle[i]) - 1:
                print('_', end='')
        print('_' * (n - len(pascal_triangle[i])))


print_pascal_triangle(create_pascal_triangle(int(input())))
