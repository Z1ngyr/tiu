from math import *

d_stand = 115000
d_lyi = 45000
d_bullet = 5600

count_lyi = 0
for i in range(5):
    stdin = input().split()
    offset_g, offset_v = int(stdin[0]), int(stdin[1])

    if sqrt((0 - offset_g) ** 2 + (0 - offset_v) ** 2) + d_bullet / 2 <= d_lyi / 2:
        pass
    else:
        count_lyi += 1
count_stand = 0
for i in range(5):
    stdin = input().split()
    offset_g, offset_v = int(stdin[0]), int(stdin[1])

    if sqrt((0 - offset_g) ** 2 + (0 - offset_v) ** 2) + d_bullet / 2 <= d_stand / 2:
        pass
    else:
        count_stand += 1
print(count_lyi, count_stand, sep='\n')
