import random
import time

def start_game():
    print("カードゲームを始めます！")
    print("目標値に最も近い合計を作りましょう。(でも超えたら負けです)")

    target_value = random.randint(15, 25)
    player_score = 0
    computer_score = 0

    while True:
        print("------------------------------")
        print(f"目標値: {target_value}")
        print(f"現在のスコア: プレイヤー {player_score} - コンピュータ {computer_score}")
        
        if player_score > target_value:
            print("あなたの数字は目標値を超えました！！")
            time.sleep(1)
            print("コンピュータの勝ち！")
            break

        if computer_score > target_value:
            print("コンピュータの数字は目標値を超えました！！")
            time.sleep(1)
            print("あなたの勝ち！")
            break
        
        print("プレイヤーのターン:")
        player_choice = input("カードを引きますか？ (y/n): ")

        if player_choice.lower() == "y":
            card_value = random.randint(1, 10)
            player_score += card_value
            print(f"引いたカードの値: {card_value}   カードの合計{player_score}")
            print()
            time.sleep(1)
        elif player_choice.lower() == "n":
            print("プレイヤーはカードを引きませんでした。")
            print()
            time.sleep(1)
        else:
            print("無効な選択です。もう一度選んでください。")

            time.sleep(1)
            continue

        print("コンピュータのターン:")

        if computer_score < target_value and (target_value - computer_score) >= 5:
            card_value = random.randint(1, 10)
            computer_score += card_value
            print(f"コンピュータがカードを引きました。")
            print(f"引いたカードの値: {card_value}  カードの合計{computer_score}")
            print()
            time.sleep(1)
        else:
            print("コンピュータはカードを引きませんでした。")
            time.sleep(1)
            if player_choice.lower() == "n":
                print("お互いにカードを引きませんでした")
                time.sleep(1)
                player_difference = target_value - player_score
                computer_difference = target_value - computer_score

                if player_difference < computer_difference:
                    print("プレイヤーの勝利です！")
                    time.sleep(1)
                    break
                elif computer_difference < player_difference:
                    print("コンピュータの勝利です！")
                    time.sleep(1)
                    break
                else:
                    print("引き分けです！")
                    time.sleep(1)
                    break

    print("------------------------------")
    print("ゲーム終了です！")
    


start_game()
