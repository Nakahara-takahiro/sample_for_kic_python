import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("１から１００までの数字を当ててください")
    print()
    while True:
        guess = int(input("1から100までの数字を入力してください: "))
        attempts += 1

        if guess < secret_number:
            print("もっと大きな数です！")
        elif guess > secret_number:
            print("もっと小さな数です！")
        else:
            print(f"正解です！{attempts}回目の予想で当たりました！")
            break

guess_number()
