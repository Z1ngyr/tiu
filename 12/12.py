n = int(input())
arr = [int(i) for i in input().split()]
arr_count = [0] * (n + 1)
for el in arr:
    arr_count[el] += 1
max = 0
count = 0
for i in range(n + 1):
    if arr_count[i] >= count and i > max:
        count = arr_count[i]
        max = i
print(max)
