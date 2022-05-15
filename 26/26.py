def fun(numbers, count):
    for i in range(count - 1):  #
        for j in range(i + 1, count - 1):
            two_numbers = set(numbers[i]) | set(numbers[j])
            if len(two_numbers) < 6:  # из 2 чисел должно получиться 7 цифр, чтобы найти третье число
                continue

            for k in range(j + 1, count):
                if len(two_numbers | set(numbers[k])) == 10:
                    return numbers[i], numbers[j], numbers[k]


n = int(input())
for i in range(n):
    m = int(input())
    lst = sorted(input().split(), key=lambda x: -len(set(x)))
    print(*fun(lst, m))
