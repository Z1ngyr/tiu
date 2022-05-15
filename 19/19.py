n = int(input())
a = [int(i) for i in input().split()]
sum_vasya = 0
sum_petya = 0
flag_petya = True
i=0
while i<len(a)-2:
    if a[i]>a[i+1]:
        sum_petya+=a[i]+a[i+2]
        sum_vasya+=a[i+1]
    else:
        sum_petya+=a[i]
        sum_vasya+=a[i+1]+a[i+2]
    i+=2
if sum_petya>sum_vasya:
    print('Vasya')
else:
    print('Petya')
