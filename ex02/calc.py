from cProfile import label
import tkinter as tk
import tkinter.messagebox as tkm



def click(event):
    btn = event.widget
    num = int(btn["text"])
    tkm.showinfo(f"{num}", f"「{num}のボタンが押されました」")

root =tk.Tk()
root.geometry("300x500")
r=0
c=0
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

root.mainloop()