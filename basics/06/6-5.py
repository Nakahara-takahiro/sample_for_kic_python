a = [5 , 4 , 3 , 6 , 2 , 1]
print(a)
b = len(a)
for i in range(b):
    c = i
    for j in range(i + 1, b):
        if a[c] > a[j]:
            c = j
    a[i], a[c] = a[c], a[i]
print(a)
