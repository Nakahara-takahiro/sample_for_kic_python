h = float(input("身長は"))
w = float(input("体重は"))
rohrer = w / (h ** 3) * (10 ** 7)
sw = (h - 100) * 0.9
himan = (w - sw) / sw * 100
print("あなたのローレル指数は", rohrer)
print("あなたの肥満度（%）は", himan)
