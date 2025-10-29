import random
import time

# 配列（リスト）を作る
fruits = ["りんご", "みかん", "ぶどう", "もも", "バナナ", "いちご"]

print("🍇 くだものスロットマシン 🎰")
print("----------------------------")

# スロットを3回まわす
for i in range(3):
    print(f"\n{i + 1}回目のチャレンジ！")
    time.sleep(1)

    # ランダムに3つのくだものを選ぶ
    slot = [random.choice(fruits), random.choice(fruits), random.choice(fruits)]

    # リストを見やすく表示（スペース区切りにする）
    print("スロットの結果：", " | ".join(slot))

    # すべて同じなら「あたり！」
    if slot[0] == slot[1] == slot[2]:
        print("🎉 あたり！すごい！ 🎉")
    else:
        print("おしい！もう一回チャレンジしてみよう！")

print("\nゲーム終了！また遊んでね😊")
