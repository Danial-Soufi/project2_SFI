a = [0, 5, 2, 10, 3]
maximum = float('-inf')
for v in a[1:]:
    if v > maximum:
        maximum = v

print( maximum)
