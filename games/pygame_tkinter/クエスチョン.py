def start_game():
    print("クイズゲームを始めます！")
    print("各質問に対して正しい選択肢を選んでください。正解するとポイントを獲得します。")

    questions = [
        {
            "question": "Pythonの作者は誰ですか？",
            "choices": ["Guido van Rossum", "Linus Torvalds", "Bill Gates"],
            "correct_choice": 0,
            "points": 10
        },
        {
            "question": "Pythonのバージョン3系列で最新のバージョンは何ですか？",
            "choices": ["3.11", "3.7", "3.8", "3.9"],
            "correct_choice": 0,
            "points": 10
        },
        {
            "question": "Pythonでインデントの単位は何文字ですか？",
            "choices": ["2文字", "3文字", "4文字", "タブ"],
            "correct_choice": 2,
            "points": 10
        }
    ]

    total_points = 0

    for question in questions:
        print("------------------------------")
        print(question["question"])
        choices = question["choices"]

        for i, choice in enumerate(choices):
            print(f"{i+1}: {choice}")

        user_choice = input("選択肢の番号を入力してください: ")

        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= len(choices):
                if user_choice - 1 == question["correct_choice"]:
                    print("正解です！ポイントを獲得しました！")
                    total_points += question["points"]
                else:
                    print("不正解です！")
            else:
                print("無効な選択です。もう一度選んでください。")
        except ValueError:
            print("無効な選択です。もう一度選んでください。")

    print("------------------------------")
    print(f"ゲーム終了です！獲得したポイント: {total_points}")

start_game()
