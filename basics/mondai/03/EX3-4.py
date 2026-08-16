a = 1.21
b = 1.20
c = 1.19
d = 1.1

e = float(input("値札の値段は＞"))
f = float(input("日本円の対ドルレートは＞"))

print("ベルギー（21%）", e * a)
print("フランス（20%）", e * b)
print("ドイツ（19%）", e * c)
print("日本（1$=", f, "円）", e * f * d)
