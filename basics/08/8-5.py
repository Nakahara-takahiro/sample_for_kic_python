import random

a = int(input("最大数はいくつにしますか？"))
print("1から" , a , "までの数を当てよう")
b = random.randint(1, a)
c = 0
while c != b:
    c = int(input("答えだと思う数字を入力＞"))
    if c < b:
        print("もっと大きい数です")
    elif c > b: 
        print("もっと小さい数です")
print("正解です！　答えは", b , "でした")
