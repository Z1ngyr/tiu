n = int(input())
count = n
for i in range(1, n + 1):
    number = str(i)
    for num in number:
        if number.count(num) != 1:
            count -= 1
            break
print(count)
