n = int(input())
p = input().split()
m = int(input())
q = input().split()

dict_p = {i:0 for i in range(max(n,m))}
dict_q = {}
for i in range(n,-1,-1):
    dict_p[i] = int(p[n-i])

for i in range(m,-1,-1):
    dict_q[i] = int(q[m-i])
    if i in dict_p:
        dict_p[i] += dict_q[i]
    else:
        dict_p[i] = dict_q[i]

print(max(dict_p))
ans = [i for i in reversed(dict_p.values())]
print(*ans)

