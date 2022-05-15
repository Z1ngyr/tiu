input()
arr = [int(i) for i in input().split()]
print(len(arr)-len(set(arr)))