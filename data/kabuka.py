# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())#取引日数
s = input().rstrip().split(' ')
m = int(s[0]) #所持金額
a = int(s[1]) #適正株価
p = [] #株価
for i in range(n):
    p.append(int(input()))

#株式購入
k = 0 #保有株数
for i in range(n):
    if p[i]<=a :
        while p[i]<=m:
            m -= p[i]
            k += 1
            
    else:
        m = m + p[i]*k
        k = 0
print(m + p[i]*k)