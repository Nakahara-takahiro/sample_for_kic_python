import time, random
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

#ゲームの設定
GAME_SPEED = 2 #モグラの入れ替わる速度[秒]

#キーパッドの初期設定
IN_PIN = [19, 20, 21, 22]#←a,b,c,d自分の配線にあわせること
SEL_PIN = [16, 17, 18]#←x,y,z自分の配線にあわせること

KEY_MAP =[[ '.','7','4','1'],
          [ '0','8','5','2'],
          [ '\n','9','6','3']]

sel_sw = []
in_sw = []

#SELピンの初期化
for i in range(len(SEL_PIN)):
    sel_sw.append(Pin(SEL_PIN[i], Pin.OUT))
    sel_sw[i].value(1)

#INピンの初期化
for i in range(len(IN_PIN)):
    in_sw.append(Pin(IN_PIN[i], Pin.IN))

#キー入力の関数
def inputKeypad():
    value = None
    for i in range(len(SEL_PIN)):
        sel_sw[i].value(0)
        for j in range(len(IN_PIN)):
            if in_sw[j].value() == 0:              
                value = KEY_MAP[i][j]
                while in_sw[j].value()==0:
                    time.sleep(0.05)
        sel_sw[i].value(1)
    return value

#モグラを表示する関数
def dispMole(molematrix):
    oled.fill(0)
    for x in range(3):
        for y in range(3):
            if molematrix[y][x]==1:
                oled.fill_rect(12*(x + 1)+30*x, 5+23*y  , 12,12,1)
    oled.show()
    
#モグラの位置
def initMole(moleline):
    moleMatrix=[ moleline[i:i+3] for i in range(0, len(moleline),3)]
    dispMole(moleMatrix)

    moleline = sum(moleMatrix, [])
    return moleline

#ゲームスタートのカウントダウン
def startCountdown():
    for i in range(3,0,-1):
        oled.fill(0)
        oled.text(str(i), 50,28)
        oled.show()
        time.sleep(1)
    oled.fill(0)
    oled.text('Game Start!', 20, 28)
    oled.show()
    time.sleep(1)
    
#ディスプレイの初期化
WIDTH = 128
HEIGHT = 64

i2c = I2C(0)
i2c.scan()

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

startCountdown()


#モグラの初期状態
initmoleline=[random.randint(0,1) for i in range(9)]
moleline = initMole(initmoleline)
t1 = time.time()

keycount = 0
molecount = initmoleline.count(1)
score = 0

while True:
    t2 = time.time()
    value = inputKeypad()
    
    #モグラを叩いたら消える
    if value != None and value != '.' and value != '0' and value != '\n':
        keycount += 1
        print('value:',value)
        if moleline[int(value)-1]==1:
            score += 1
        moleline[int(value)-1]=0
        initMole(moleline)
    
    #モグラの再設置（全滅or指定時間経過）
    if 1 not in moleline or t2 - t1 > GAME_SPEED:
        t1 = time.time()
        moleline = [random.randint(0,1) for i in range(9)]
        initMole(moleline)
        molecount += moleline.count(1)
        print(molecount)
    
    #終了条件
    if keycount >=50 or molecount >= 100:
        break

#スコア表示
oled.fill(0)
oled.text('Score:' + str(score), 30, 8)
oled.text('Try again!', 25,30)
oled.text('press enter', 20,50)
oled.show()

#ソフトウエアリブート（main.pyで保存していると再スタート）
while True:
    value = inputKeypad()

    if value == '\n':
        machine.soft_reset()