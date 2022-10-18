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

def key_down(event):
    global key,mod
    key=event.keysym
    if key=="w":
            mod=1
    if key=="n":
        mod=0  
    restert()
    if mod==1:
        main_proc2()
    else: 
        main_proc()
    goal()

def key_up(event):
    global key
    key=""

def main_proc():
    global key,mx,my,cx,cy
    if key=="Up":
        if maze_list[my-1][mx]==0:
            my-=1
            cy-=100
    elif key=="Down":
        if maze_list[my+1][mx]==0:
            my+=1
            cy+=100
    elif key=="Left":
        if maze_list[my][mx-1]==0:
            mx-=1
            cx-=100
    elif key=="Right":
        if maze_list[my][mx+1]==0:
            mx+=1
            cx+=100
    #print(f"{mx}")
    canvas.coords("tori",cx,cy)

def main_proc2():
    global key,mx,my,cx,cy,mod
    if key=="Up":
        if maze_list[my-1][mx]==1:
            my-=1
            cy-=100
    elif key=="Down":
        if maze_list[my+1][mx]==1:
            my+=1
            cy+=100
    elif key=="Left":
        if maze_list[my][mx-1]==1:
            mx-=1
            cx-=100
    elif key=="Right":
        if maze_list[my][mx+1]==1:
            mx+=1
            cx+=100
    canvas.coords("tori",cx,cy)




def restert():
    global cx ,cy,key,mx,my,maze_list,tori,mod
    if key=="r":
        maze_list=maze_maker.make_maze(15,9)
        maze_maker.show_maze(canvas,maze_list) 
        cx=150
        cy=150
        mx=1
        my=1
        canvas.create_text(
            150,
            40 ,
            font=("", 20),
            text="[Nキー]ノーマルモード\n[Wキー]壁モード\n[Rキー]再起動")
        canvas.lift("tori",)
        mod=0
        makea_goll()

def makea_goll():
    global maze_list,ans1,ans2
    gool=[]
    for nam,i in enumerate(maze_list):
        for num2,j in enumerate (i):
            if j==0:
                if i[num2-1]==1 and i[num2+1]==1 and maze_list[nam-1][num2]==1:
                    gool.append((nam,num2))
                if i[num2-1]==1 and i[num2+1]==1 and maze_list[nam+1][num2]==1:
                    gool.append((nam,num2))
                if i[num2+1]==1 and maze_list[nam-1][num2]==1 and maze_list[nam+1][num2]==1:
                    gool.append((nam,num2))
                if  i[num2-1]==1 and maze_list[nam-1][num2]==1 and maze_list[nam+1][num2]==1:
                    gool.append((nam,num2))   

    len1=len(gool)
    nam=randint(1,len1-1)
    ans=gool[nam] 
    ans1,ans2=ans
    canvas.create_rectangle(100, 100, 200,200, fill = 'green',tag="red") 
    canvas.create_rectangle(ans2*100, ans1*100, ans2*100+100,ans1*100+100 , fill = 'red',tag="red") 
    canvas.lift("tori","red")   

def goal():
    global ans1,ans2,mx,my,maze_list
    if ans1==my and ans2==mx:
        canvas.create_text(
            1500 // 2,
            900 // 2,
            font=("", 80),
            text="       ゲームクリア！\n[Rキー]で再起動してね"
        )
        maze_list=1
        
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

tori=tk.PhotoImage(file="ex03/fig/"+str(randint(0,9))+".png")
canvas.create_image(cx,cy,image=tori,tag="tori")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas.create_text(
            150,
            40 ,
            font=("", 20),
            text="[Nキー]ノーマルモード\n[Wキー]壁モード\n[Rキー]再起動")
makea_goll()
root.mainloop()