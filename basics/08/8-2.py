import time

def genzan(a):
    while(a):
        print(a)
        time.sleep(1)
        a -= 1
    print("時間です！")

a = input("何秒をカウントダウンしますか＞")
genzan(int(a)) 
