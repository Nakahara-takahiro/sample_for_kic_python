a = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
b = input("探す曜日の一部を英語で入力＞")
c = [ s for s in a if s.find(b) > -1]
print(c, "発見！")
