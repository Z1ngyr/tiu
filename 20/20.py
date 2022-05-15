n = int(input())
arr = [[0] * n for i in range(n)]
arr_numbers = [i for i in range(1, n * (n - 1) + 1)]
next = 0
for i in range(n):
    for j in range(n):
        if i != j:
            arr[i][j] = arr_numbers[next]
            next += 1
    print(*arr[i])
