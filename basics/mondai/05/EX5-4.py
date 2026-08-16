print("腹立つ返信コンピュータ：終了は「さようなら」と入力")

while True:
    a = input("あなた：")
    if a == "さようなら":
        break
    if a == "おはよう":
        print("おはよう")
        continue
    print("コンピュータ: " , a , "って言いましたけど、あなたの感想ですよね？")
