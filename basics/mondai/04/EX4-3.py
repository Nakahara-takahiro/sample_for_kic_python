h = float(input("身長は"))
h = h / 100.0
w = float(input("体重は"))
bmi = w / (h ** 2)
print("あなたのBMI=", bmi)
if bmi < 18.5:
    print("低体重")
elif bmi < 25:
    print("普通体重")
else:
    print("肥満")
