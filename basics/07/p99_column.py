def bubble_sort(a, b):
    for i in range(b):
        for j in range(b-1, i, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

a = ["Fortrun" , "COBOL" , "BASIC" , "C" , "Java" , "Python"]
print(bubble_sort(a , len(a)))
