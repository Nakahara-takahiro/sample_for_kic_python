import random

a1 = int(input("最小数はいくつにしますか？"))
a2 = int(input("最大数はいくつにしますか？"))
print( a1 , "から" , a2 , "までの数を当てよう")
b = random.randint(a1, a2)
c = 0
while c != b:
    c = int(input("答えだと思う数字を入力＞"))
    if c < b:
        print("もっと大きい数です")
    elif c > b: 
        print("もっと小さい数です")
print("正解です！　答えは", b , "でした")
