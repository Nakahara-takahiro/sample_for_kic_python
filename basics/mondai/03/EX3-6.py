a = float(input("単価は"))
b = float(input("購入数は"))
c = float(input("税率（％）は"))
print("支払金額は", int(a * b * (c / 100 + 1)), "円")
