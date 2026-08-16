i = 0

a = int(input (">>"))
while i < 4:
    b = int(input (">>"))
    if(a > b):
        a = b
    i = i + 1
print("最小値は" , a)
