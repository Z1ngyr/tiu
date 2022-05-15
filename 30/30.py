# спасибо за задачу из яндекса)
# на чет позициях - нечетные числа
# на нечет позициях - четные

n = int(input())
numbers = input().split()
arr = [0] * n
kol_vo_ed_na_chet_pos = 0
kol_vo_ed_na_nechet_pos = 0
kol_vo_chet = 0
kol_vo_nechet = 0
for i in range(n):
    arr[i] = int(numbers[i])
    if i % 2 == 0 and arr[i] % 2 != 0:
        kol_vo_ed_na_chet_pos += 1
    if i % 2 != 0 and arr[i] % 2 != 0:
        kol_vo_ed_na_nechet_pos += 1
    if arr[i] % 2 != 0:
        kol_vo_nechet += 1
    else:
        kol_vo_chet += 1
if abs(kol_vo_nechet - kol_vo_chet > 1):
    print(-1)
else:

    arr_chet = []
    arr_nechet = []
    arr_new = [-1] * n

    if kol_vo_ed_na_chet_pos > kol_vo_ed_na_nechet_pos:
        for i in range(n):
            if i % 2 == 0:
                if arr[i] % 2 != 0:
                    arr_new[i] = arr[i]
                else:
                    arr_chet.append(arr[i])
            elif arr[i] % 2 == 0:
                arr_new[i] = arr[i]
            else:
                arr_nechet.append(arr[i])

        count = 0
        for i in range(n):
            if arr_new[i] == -1:
                count += 1
                if i % 2 == 0:
                    arr_new[i] = arr_nechet[0]
                    arr_nechet.pop(0)
                else:
                    arr_new[i] = arr_chet[0]
                    arr_chet.pop(0)
        print(count)
        print(*arr_new)

    else:
        for i in range(n):
            if i % 2 == 0:
                if arr[i] % 2 == 0:
                    arr_new[i] = arr[i]
                else:
                    arr_nechet.append(arr[i])
            elif arr[i] % 2 != 0:
                arr_new[i] = arr[i]
            else:
                arr_chet.append(arr[i])
        count = 0
        for i in range(n):
            if arr_new[i] == -1:
                count += 1
                if i % 2 == 0:
                    arr_new[i] = arr_chet[0]
                    arr_chet.pop(0)
                else:
                    arr_new[i] = arr_nechet[0]
                    arr_nechet.pop(0)
        print(count)
        print(*arr_new)
