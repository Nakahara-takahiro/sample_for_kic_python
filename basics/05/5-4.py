i = 1

a = int(input (">>"))
while i < 5:
    b = int(input (">>"))
    if(a > b):
        a = b
    i = i + 1
print("最小値は" , a)
