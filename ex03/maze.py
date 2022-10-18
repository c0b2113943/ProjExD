import tkinter as tk
cx=300
cy=400
key=""

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
root.mainloop()