import tkinter as tk
import random

SIZE = 30       #ブロックのサイズ
moveX = 4       #テトロミノ表示位置（横）
moveY = 0       #テトロミノ表示位置（縦）
type = random.randint(0, 6)        #テトロミノのタイプ

timer = 800     #ゲームスピードコントロール

color = ["magenta", "blue", "cyan", "yellow", "orange", "red", "green", "black", "white"]

#テトロミノデータ
tetroT = [-1, 0, 0, 0, 1, 0, 0, 1]
tetroJ = [-1, 0, 0, 0, 1, 0, 1, 1]
tetroI = [-1, 0, 0, 0, 1, 0, 2, 0]
tetroO = [ 0, 0, 1, 0, 0, 1, 1, 1]
tetroL = [-1, 0, 0, 0, 1, 0,-1, 1]
tetroZ = [-1,-1, 0,-1, 0, 0, 1, 0]
tetroS = [ 0, 0, 1, 0, 0, 1,-1, 1]
tetro = [tetroT, tetroJ, tetroI, tetroO, tetroL, tetroZ, tetroS]

#フィールドデータ
field = []
for y in range(22):
    sub = []
    for x in range(12):
        if x==0 or x==11 or y==21 :
            sub.append(8)
        else :
            sub.append(7)
    field.append(sub)

#テトロミノを表示する関数
def drawTetris():
    for i in range(4):
        x = (tetro[type][i*2]+moveX)*SIZE
        y = (tetro[type][i*2+1]+moveY)*SIZE
        can. create_rectangle(x, y, x+SIZE, y+SIZE, fill=color[type])

#フィールドを表示する関数
def drawField():
    for i in range(21):
        for j in range(12):
            outLine=0 if color[field[i+1][j]]=="white" else 1   #白いブロックは枠無しで表示
            can.create_rectangle(j*SIZE, i*SIZE, (j+1)*SIZE, (i+1)*SIZE, fill=color[field[i+1][j]], width=outLine)



def judge(afterX, afterY, afterTetro):  #アタリ判定をする関数
    global moveX, moveY
    result = True
    for i in range(4):
        x = afterTetro[i*2]+afterX
        y = afterTetro[i*2+1]+afterY
        if field[y+1][x]!=7 :
            result = False
    if result==True :
        moveX = afterX
        moveY = afterY
        tetro[type].clear()
        tetro[type].extend(afterTetro)
    return result

def dropTetris():
    global moveX, moveY, type, timer
    afterTetro = []
    afterTetro.extend(tetro[type])
    result = judge(moveX, moveY+1, afterTetro)
    if result==False :
        for i in range(4):
            x = tetro[type][i*2]+moveX
            y = tetro[type][i*2+1]+moveY
            field[y+1][x] = type
        type = random.randint(0, 6)
        moveX = 4
        moveY = 0
    can.after(timer, dropTetris)
    timer -= 2                          #落下速度コントロール
    if timer<140 :
        timer = 180

win = tk.Tk()
win.geometry("340x630")
can = tk.Canvas(win, width=12*SIZE, height=21*SIZE)
can.place(x=-10, y=0)
var = tk.StringVar()
lab = tk.Label(win, textvariable=var, fg="blue", bg="white", font=("", "20"))   #得点表示
lab.place(x=50, y=600)


def gameLoop():
    can.delete("all")
    drawField()
    drawTetris()
    can.after(50, gameLoop)

gameLoop()
dropTetris()
win.mainloop()