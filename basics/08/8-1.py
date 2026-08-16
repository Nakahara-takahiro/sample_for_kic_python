import datetime

w = ["月", "火" , "水" , "木" , "金" , "土" , "日"]

y = int(input("何年生まれ？＞"))
m = int(input("何月生まれ？＞"))
d = int(input("何日生まれ？＞"))
a = datetime.date(y , m , d)

print("あなたは" , w[a.weekday()] , "曜日に生まれました")
