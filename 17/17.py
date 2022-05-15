n = int(input())
time_list = []  # содержит список кортежей времени нач и конц
for i in range(n):
    time_list.append(tuple(map(int, input().split())))
time_list.sort(key=lambda x: x[0], reverse=True)

time_max = t = 0
for i, s in enumerate(time_list):
    time = sum(int(time_list[j][1] >= s[0]) for j in range(i, len(time_list)))
    if time >= time_max:
        time_max = time
        t = s[0]

print(t)
