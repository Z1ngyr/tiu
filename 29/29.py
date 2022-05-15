n = int(input())
p = input().split()
m = int(input())
q = input().split()

dict_p = {i: int(p[n - i]) for i in range(n, -1, -1)}
dict_q = {i: int(q[m - i]) for i in range(m, -1, -1)}
dict_ans = {i: 0 for i in range(n + m, -1, -1)}
for i in range(n, -1, -1):
    for j in range(m, -1, -1):
        dict_ans[i + j] += dict_p[i] * dict_q[j]
print(n + m)
ans = [i for i in dict_ans.values()]
print(*ans)
