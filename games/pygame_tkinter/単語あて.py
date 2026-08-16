import random

def start_game():
    print("単語当てゲームを始めます！")
    print("ヒントに基づいてランダムな単語を当てましょう。")

    words = ["apple", "banana", "cherry", "grape", "orange"]
    hint_messages = {
        "apple": "赤くて丸い果物",
        "banana": "黄色くて長い果物",
        "cherry": "小さくて赤い果物",
        "grape": "小さくて丸い果物",
        "orange": "オレンジ色の果物"
    }

    random_word = random.choice(words)
    hint = hint_messages[random_word]

    guessed_word = "_" * len(random_word)
    incorrect_guesses = []
    max_attempts = 5

    while True:
        print("------------------------------")
        print(f"ヒント: {hint}")
        print(f"現在の状態: {guessed_word}")
        print(f"不正解の試行回数: {len(incorrect_guesses)}/{max_attempts}")
        
        if len(incorrect_guesses) >= max_attempts:
            print("ゲームオーバー！正解は", random_word)
            break
        
        if guessed_word == random_word:
            print("正解です！おめでとうございます！")
            break

        guess = input("単語を予想してください: ").lower()

        if len(guess) != 1:
            print("1文字だけ入力してください。")
            continue

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i+1:]
        else:
            if guess in incorrect_guesses:
                print("その文字は既に試しています。")
            else:
                incorrect_guesses.append(guess)
                print("不正解です。")

    print("------------------------------")
    print("ゲーム終了です！")

start_game()
