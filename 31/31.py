n = int(input())
arr_kanon = [int(i) for i in input().split()]
arr_kanon.sort()
arr_new = []
m = int(input())
for i in range(m):
    num = int(input())
    arr_new.append(num)
    difference = 10**7
    if num<0:
        for i in range(n):
            if abs(arr_kanon[i] - num) < difference:
                difference = abs(arr_kanon[i] - num)
            else:
                print(arr_kanon[i-1])
                break
    else:
        for i in range(n-1,-1,-1):
            if abs(arr_kanon[i] - num) < difference:
                difference = abs(arr_kanon[i] - num)
            else:
                print(arr_kanon[i+1])
                break
