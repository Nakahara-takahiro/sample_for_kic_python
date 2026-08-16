#ライブラリインポート
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np
import cv2
#スロットの回転スピード
slot_speed=200
#文字サイズ&位置、画面サイズ調整
fsize1=300
fsize2=100
line_color=(255,255,255)
font_color=(255,0,0)
h=600
w=1000
string_posy=50
string_posx=70
w2=20
#文字フォント設定
font_path="C:\Windows\Fonts\HGRPP1.TTC"
font1 = ImageFont.truetype(font_path, fsize1) 
font2 = ImageFont.truetype(font_path, fsize2) 
#初期画像の作成
img=Image.new("RGB",(w,h))
draw = ImageDraw.Draw(img)
botton_pos=[]
for i in range(3):
    x1=int(i*w/3+w2)
    y1=int(w2)
    x2=int(((i+1)*w)/3-w2)
    y2=int(h-w2*10)
    botton_pos.append([[x1,y2+w2],[x2,int(h-w2)]])
    draw.rectangle(((x1, y1), (x2, y2)), fill=(0, 0, 0), outline=line_color, width=10)
    draw.rectangle(((x1, int(y2+w2)), (x2, int(h-w2))), fill=(0, 0, 0), outline=line_color, width=10)
    draw.text((int((x1+x2)/2-fsize2),int((h+y2)/2-fsize2/2)), 'STOP', font = font2 , fill = font_color)
botton_pos=np.array(botton_pos)

img2=img
draw2 = ImageDraw.Draw(img2)
num_y_pos=int(string_posy)
num_x_offset=int(string_posx)
num_pos=[(int(w/6-num_x_offset),num_y_pos),(int(w/2-num_x_offset),num_y_pos),(int(w*5/6-num_x_offset),num_y_pos)]

#完成時の画像描写
def goal(img3):
    img4=Image.fromarray(img3)
    draw4 = ImageDraw.Draw(img4)
    draw4.text((int(w/2-200),int(h/2-100)), 'Complete!', font = font2 , fill = font_color)
    img4=np.array(img4)
    img4=cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)
    cv2.imshow('window', img4)

#回転時の画像描写
num_list=np.array([1,2,3])
def draw_num(num_list):
    img3=np.copy(np.array(img2))
    img3=Image.fromarray(img3)
    draw3 = ImageDraw.Draw(img3)
    for i in range(3):
        draw3.text(num_pos[i], str(num_list[i]), font = font1 , fill = font_color)
    img3=np.array(img3)
    img3=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
    cv2.imshow('window', img3)
    cv2.waitKey(slot_speed)
    if max(num_list)==min(num_list):
        goal(img3)

#回転処理
def Loop(coutner,disnum,start):
    ccc=0
    flag=1
    while max(counter)==1 and start==0:
        ccc+=1
        if ccc%10==0:
            disnum+=counter
            disnum=disnum%9
            draw_num(disnum+1)

    
#回転処理
draw_num(num_list)
start=0
counter=np.array([1,1,1])
disnum=np.array([7,8,9])
def play_slot(event, x, y, flags, params):
    global counter,disnum,ccc,start
    if event == cv2.EVENT_RBUTTONDOWN and start==0:
        counter=np.array([1,1,1])
        disnum=np.array([7,8,9])
        Loop(counter,disnum,start)            
    if event == cv2.EVENT_LBUTTONDOWN:
        if x>botton_pos[0,0,0] and x<botton_pos[0,1,0] and \
           y>botton_pos[0,0,1] and y<botton_pos[0,1,1]:
            counter[0]=min(counter[0]-1,0)
        elif x>botton_pos[1,0,0] and x<botton_pos[1,1,0] and \
             y>botton_pos[1,0,1] and y<botton_pos[1,1,1]:
            counter[1]=min(counter[1]-1,0)
        elif x>botton_pos[2,0,0] and x<botton_pos[2,1,0] and \
             y>botton_pos[2,0,1] and y<botton_pos[2,1,1]:
            counter[2]=min(counter[2]-1,0)
        start=1
    if max(counter)==0:
        start=1
        disnum=disnum%10
    if event == cv2.EVENT_RBUTTONDOWN and start!=0:
        counter=np.array([1,1,1])
        start=0

cv2.setMouseCallback('window', play_slot)
cv2.waitKey(0)
cv2.destroyAllWindows()