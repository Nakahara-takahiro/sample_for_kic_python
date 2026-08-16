def kiro_to_pound(a):
    b = a * 1000 / 453.592
    return b

def pound_to_kiro(c):
    d = c * 453.592 / 1000
    return d

e = int(input("処理番号（1:キログラム→ポンド、2:ポンド→キログラム）を入力＞"))

if e == 1:
    k = float(input("重さの入力（キログラム）＞"))
    x = kiro_to_pound(k)
    print(x, "ポンド")
elif e == 2:
    p = float(input("重さの入力（ポンド）＞"))
    y = pound_to_kiro(p)
    print(y, "キログラム")
else:
    print("終了します。")
