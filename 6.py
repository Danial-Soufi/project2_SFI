a = [11,22,33,44,66]
n = len(a)
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp

print(a)
