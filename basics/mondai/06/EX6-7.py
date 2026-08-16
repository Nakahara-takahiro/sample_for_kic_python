a = [2 , 7 , 4 , 1]
print("変更前リストa", a)
b = a
c = a.copy()
d = list(a)
a[0] = "削除"
c.sort()
d.sort(reverse=True)
print("リストa", a)
print("リストb", b)
print("リストc", c)
print("リストd", d)
