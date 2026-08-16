import random

def start_game():
    print("ハングマンゲームを始めます！")
    print("ランダムに選択された単語を当てましょう。")
    print("試行回数は２０回までです。")

    words = ["apple", "banana", "cherry", "grape", "orange"]
    random_word = random.choice(words)
    guessed_letters = []
    max_attempts = 20
    attempts=0
    while True:
        print("------------------------------")
        print("現在の状態: ", end="")
        print("試行回数",attempts,"/20回")
        for letter in random_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print("\n")

        if set(guessed_letters) == set(random_word):
            print("正解です！おめでとうございます！")
            break

        if len(guessed_letters) >= max_attempts:
            print("ゲームオーバー！正解は", random_word)
            break

        guess = input("予想した文字を入力してください: ").lower()
        
        attempts +=1

        if len(guess) != 1 or not guess.isalpha():
            print("1文字のアルファベットを入力してください。")
            continue

        if guess in guessed_letters:
            print("その文字は既に予想されています。")
            continue
        if guess in random_word:
            guessed_letters.append(guess)

        if guess not in random_word:
            print("不正解です。")
        
    print("------------------------------")
    print("ゲーム終了です！")

start_game()
