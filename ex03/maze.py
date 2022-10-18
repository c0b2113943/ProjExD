import tkinter as tk
import maze_maker
cx=150
cy=150
key=""
mx=1
my=1

def key_down(event):
    global key
    key=event.keysym
    main_proc()

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

tori=tk.PhotoImage(file="ex03/fig/5.png")
canvas.create_image(cx,cy,image=tori,tag="tori")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

root.mainloop()