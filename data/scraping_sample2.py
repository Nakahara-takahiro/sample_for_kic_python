import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re 
import time 

url="https://www.yahoo.co.jp/"

req=requests.get(url)

soup=BeautifulSoup(req.content,"html.parser")

elems=soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

num=len(elems)

news=np.zeros((num,3),dtype='object')

i=0
for elem in elems:
    res_detail=requests.get(elem.attrs['href'])
    soup_detail=BeautifulSoup(res_detail.content,"html.parser")

    elems_detail=soup_detail.find(class_=re.compile("highLightSearchTarget"))

    news[i][0]=elem.text
    news[i][1]=elem.attrs['href']

    if elems_detail is not None:
        news[i][2]=elems_detail.text
    else:
        news[i][2]=None
    time.sleep(1)
    i=i+1
df=pd.DataFrame(news,columns=["title","url","highlight"])
df.to_csv("data_pandus_n.csv",index=False,encoding="utf-8-sig")