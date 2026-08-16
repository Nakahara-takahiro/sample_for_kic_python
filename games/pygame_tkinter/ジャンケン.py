import random

def play_game():
    choices = ["グー", "チョキ", "パー", "終了"]
    computer_choice = random.choice(choices)

    print("じゃんけんゲームを始めます！")
    print("1: グー")
    print("2: チョキ")
    print("3: パー")
    print("4: 終了")

    user_choice = int(input("選択肢の番号を入力してください: ")) - 1
    user_choice = choices[user_choice]

    print(f"あなたの選択: {user_choice}")
    print(f"コンピューターの選択: {computer_choice}")

    if user_choice == "終了":
        print("ありがとうございました")
        exit()
    elif user_choice == computer_choice:
        print("引き分けです！")
    elif (
        (user_choice == "グー" and computer_choice == "チョキ") or
        (user_choice == "チョキ" and computer_choice == "パー") or
        (user_choice == "パー" and computer_choice == "グー")
    ):
        print("あなたの勝ちです！")
    else:
        print("コンピューターの勝ちです！")

if __name__=="__main__":
    while True:
        play_game()
    