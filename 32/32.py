s = input()

elements = {'0': [], '1': []}
arr = []
temp = ''
for i in range(len(s)):
    now = temp + s[i]
    if now in elements[now[0]]:
        temp += s[i]
    else:
        elements[now[0]].append(now)
        arr.append(now)
        temp = ''
if temp != '':
    arr.append(temp)
print(*arr)
