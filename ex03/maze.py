import tkinter as tk
cx=300
cy=400
key=""

def key_down(event):
    global key
    key=event.keysym
    main_proc()

def key_up(event):
    global key
    key=""

def main_proc():
    global key,cx,cy
    if key=="Up":
        cy-=20
    elif key=="Down":
        cy+=20
    elif key=="Left":
        cx-=20
    elif key=="Right":
        cx+=20
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

tori=tk.PhotoImage(file="ex03/fig/5.png")
canvas.create_image(cx,cy,image=tori,tag="tori")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

root.mainloop()