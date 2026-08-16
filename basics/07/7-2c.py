a = 5

def sankaku():
    global a
    a = 4
    b = 8
    print(a * b / 2)

sankaku()
print(a)
