import tkinter as tk
import maze_maker
from random import randint
cx=150
cy=150
key=""
mx=1
my=1
ans1=0
ans2=0
mod=0
kai=1
def key_down(event):
    global key,mod
    key=event.keysym
    if key=="w":     #モード切替
        mod=1        #壁モード
    if key=="n":
        mod=0      #ノーマルモード
    restert()
    if mod==1:
        main_proc2()
    else: 
        main_proc()
    goal()

def key_up(event):
    global key
    key=""

def main_proc():             #ノーマルモードでの動き（道を進む）
    global key,mx,my,cx,cy
    if key=="Up":
        if maze_list[my-1][mx]==0: #動こうとしている先のmaze_list（０と１の行列）を見て道なら現在位置を更新する
            my-=1
            cy-=100
    elif key=="Down":
        if maze_list[my+1][mx]==0: #動こうとしている先のmaze_list（０と１の行列）を見て道なら現在位置を更新する
            my+=1
            cy+=100
    elif key=="Left":
        if maze_list[my][mx-1]==0: #動こうとしている先のmaze_list（０と１の行列）を見て道なら現在位置を更新する
            mx-=1
            cx-=100
    elif key=="Right":
        if maze_list[my][mx+1]==0: #動こうとしている先のmaze_list（０と１の行列）を見て道なら現在位置を更新する
            mx+=1
            cx+=100
    #print(f"{mx}")
    canvas.coords("tori",cx,cy)

def main_proc2():               #壁モードの動き（壁の中を動く。道は進めない）
    global key,mx,my,cx,cy,mod
    if key=="Up":
        if maze_list[my-1][mx]==1 :#動こうとしている先のmaze_list（０と１の行列）を見て壁なら現在位置を更新する
            my-=1
            cy-=100
    elif key=="Down":
        if maze_list[my+1][mx]==1:#動こうとしている先のmaze_list（０と１の行列）を見て壁なら現在位置を更新する
            my+=1
            cy+=100
    elif key=="Left":
        if maze_list[my][mx-1]==1:#動こうとしている先のmaze_list（０と１の行列）を見て壁なら現在位置を更新する
            mx-=1
            cx-=100
    elif key=="Right":
        if maze_list[my][mx+1]==1:#動こうとしている先のmaze_list（０と１の行列）を見て壁なら現在位置を更新する
            mx+=1
            cx+=100
    canvas.coords("tori",cx,cy)

def restert():                      #ゴールをしRキーを押したときに再起動する
    global cx ,cy,key,mx,my,maze_list,tori,mod,kai
    if key=="r"and ans1==my and ans2==mx:
        kai+=1
        maze_list=maze_maker.make_maze(15,9)   #新しいmaze_list（０と１の行列）を使い描画し直す
        maze_maker.show_maze(canvas,maze_list) 
        cx=150
        cy=150
        mx=1
        my=1
        canvas.create_text(
            150,
            40 ,
            font=("", 20),
            text=f"[Nキー]ノーマルモード\n[Wキー]壁モード\n{kai}階"
            )
        canvas.lift("tori",)  #こうかとんを前面に持ってくる
        mod=0
        makea_goll()

def makea_goll():             #ゴールを作成する。道であり三方を壁に囲まれた行き止まりをゴールの候補として得る。
    global maze_list,ans1,ans2
    gool=[]
    for nam,i in enumerate(maze_list):
        for num2,j in enumerate (i):
            if j==0:
                if i[num2-1]==1 and i[num2+1]==1 and maze_list[nam-1][num2]==1:    #下以外が壁の時
                    gool.append((nam,num2))
                if i[num2-1]==1 and i[num2+1]==1 and maze_list[nam+1][num2]==1:    #上以外が壁の時
                    gool.append((nam,num2))
                if i[num2+1]==1 and maze_list[nam-1][num2]==1 and maze_list[nam+1][num2]==1:   #左以外が壁の時
                    gool.append((nam,num2))
                if  i[num2-1]==1 and maze_list[nam-1][num2]==1 and maze_list[nam+1][num2]==1:  #右下以外が壁の時
                    gool.append((nam,num2))   

    len1=len(gool)        #ゴールの候補の長さを取る。
    nam=randint(1,len1-1) #0番はスタートが入ってくることがあるので除きそれ以外の候補から選ぶ
    ans=gool[nam] 
    ans1,ans2=ans
    canvas.create_rectangle(100, 100, 200,200, fill = 'green',tag="red")    #スタートを緑にする
    canvas.create_rectangle(ans2*100, ans1*100, ans2*100+100,ans1*100+100 , fill = 'red',tag="red") #選ばれたゴールの場所を赤くする
    canvas.lift("tori","red")   #こうかとんを前面に持ってくる

def goal():        #ゴール判定
    global ans1,ans2,mx,my,maze_list,kai
    if ans1==my and ans2==mx:       #上で選ばれゴールについたらメッセ時を表示
        canvas.create_text(        
            1500 // 2,
            900 // 2,
            font=("", 80),
            text=f"    {kai}階層クリア！\n[Rキー]で{kai+1}層へ"
        )
        maze_list=2      #全てを壁でも道でも無いものにし、動けなくする
        
root=tk.Tk()
root.title("迷えるこうかとん")
canvas=tk.Canvas(
    root,
    width=1500,
    height=900,
    bg="black"
)

canvas.pack()

maze_list=maze_maker.make_maze(15,9)
maze_maker.show_maze(canvas,maze_list)

tori=tk.PhotoImage(file="ex03/fig/"+str(randint(0,9))+".png")   #起動時はランダムなこうかとんが選ばれる
canvas.create_image(cx,cy,image=tori,tag="tori")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas.create_text(
            150,
            40 ,
            font=("", 20),
            text=f"[Nキー]ノーマルモード\n[Wキー]壁モード\n{kai}階")
makea_goll()
root.mainloop()