n = int(input())
arr = [[0] * n for i in range(n)]
arr_yet = []
for i in range(n):
    arr_temp = [int(i) for i in input().split()]
    for j in range(n):
        if arr_temp[j] != 0:
            arr[i][j] = arr_temp[j]
            arr_yet.append(arr_temp[j])
arr_yet = [i for i in range(1, n ** 2 + 1) if i not in arr_yet]
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = arr_yet[count]
            count += 1
    print(*arr[i])
