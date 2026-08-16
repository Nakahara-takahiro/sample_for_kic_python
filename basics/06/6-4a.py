a = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
b = [ s for s in a if s.find("Fri") > -1]
print(b, "発見！")
