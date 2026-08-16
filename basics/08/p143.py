from time import time

s = 0 # スタート時間
e = 0 # 終了時間
d = 0 # 差分

t = input("10 秒を当てます。Enter キーでスタートします＞")

if t in "":
    print("頭の中で計測中...")
    s = time()

t = input("Enter キーでストップします＞")
if t in "":
    print("停止！")
    e = time()

d = round(e - s, 1)

print("あなたの10 秒は：" , d , "でした。")
if d == 10.0:
    print("完璧！")
elif d >= 9.0 and d < 10.0:
    print("優秀！")
else:
    print("やり直し！")
