input()
nums = map(int, input().split(' '))
nums_count = {}

for i in nums:
    nums_count[i] = nums_count[i] + 1 if i in nums_count else 1

count = 0
for k, v in nums_count.items():
    if v == 1:
        count += 1

print(count)
