import time
def start_game():
    print()
    print()   
    print("アドベンチャーゲームを始めます！")
    print("あなたは古代の遺跡に迷い込んでしまいました。出口を見つけるためにはさまざまな謎を解かなければなりません。")
    print("さあ、冒険を始めましょう！")
    current_location = "エントランス"
    found_items = []
    solved_puzzles = []

    while True:
        print("------------------------------")
        print(f"現在の場所: {current_location}")
        print(f"現在持っているアイテム：{found_items}")

        if current_location == "エントランス":
            print("エントランスにいます。どこに進みますか？")
            print()
            print("1: 廊下")
            print("2: トラップルーム")
            print("3: 隠し通路")

            choice = input("選択肢の番号を入力してください: ")

            if choice == "1":
                current_location = "廊下"
                print()
                print("廊下に移動します")
                print()
                time.sleep(1)
            elif choice == "2":
                current_location = "トラップルーム"
                print()
                print("トラップルームに移動します")
                print()
                time.sleep(1)
            elif choice == "3":
                current_location = "隠し通路"
                print()
                print("隠し通路に移動します")
                print()
                time.sleep(1)
            else:
                print("無効な選択です。もう一度選んでください。")
                time.sleep(2)

        elif current_location == "廊下":
            print()
            print("廊下にいます。どこか調べますか？")
            print("1: 絵画を調べる")
            print("2: 床を調べる")
            print("3: 戻る")

            choice = input("選択肢の番号を入力してください: ")

            if choice == "1":
                if "鍵" not in found_items:
                    print()
                    print("絵画の裏に鍵がありました！")
                    time.sleep(1)
                    found_items.append("鍵")
                else:
                    print("何も見つかりませんでした。")
                    time.sleep(1)
            elif choice == "2":
                print("何もありませんでした")
                print()
                time.sleep(1)
            elif choice == "3":
                current_location = "エントランス"
                print()
                print("エントランスにもどります")
                time.sleep(1)
                print()
            else:
                print("無効な選択です。もう一度選んでください。")
                time.sleep(1)

        elif current_location == "トラップルーム":
            if "鍵" not in found_items:
                print("トラップルームには鍵がかかっています。鍵を見つけてから戻ってきてください。")
                time.sleep(1)
                current_location = "エントランス"
            else:
                if "鍵解除" not in solved_puzzles:
                    print()
                    print("鍵を使ってトラップルームにはいります")
                    time.sleep(1)
                    print()
                    print("罠が仕掛けられています。謎を解いて罠を解除しましょう。")
                    print("問題: 3 + 5 × 2 - 1 の答えは？")

                    answer = input("答えを入力してください: ")
                
                    if answer == "12":
                        print()
                        print("正解です！罠が解除されました！")
                        print()
                        time.sleep(1)
                        solved_puzzles.append("鍵解除")
                    else :
                        print()
                        print("不正解です！罠が作動しました！あなたはダメージを受けました。")
                        print()
                        time.sleep(1)
                        print("残念ながらゲームオーバーです")
                        time.sleep(1)
                        print()
                        break
                    
                else:
                    print("トラップルームにはもう罠はありません。")
                    print("エントランスに戻ります")
                    print()
                    time.sleep(1)
                    current_location = "エントランス"

        elif current_location == "隠し通路":
            if "鍵解除" not in solved_puzzles:
                print()
                print("隠し通路には鍵解除が必要です。他の場所を探索してください。")
                time.sleep(1)
                current_location = "エントランス"
            else:
                print()
                print("隠し通路に到着しました！出口が見えます！")
                time.sleep(1)
                print()
                print("おめでとうございます！ゲームクリアです！")
                break

  

        

start_game()
print("ゲーム終了です！お疲れ様でした！")
time.sleep(1)
print()