from cProfile import label
import tkinter as tk
import tkinter.messagebox as tkm



def click(event):  #練習３
    btn = event.widget
    num = int(btn["text"])
    #tkm.showinfo(f"{num}", f"「{num}のボタンが押されました」")
    entry.insert(tk.END, num) #5

def click2(event):  #6
    btn = event.widget
    num = str(btn["text"])
    entry.insert(tk.END, num) 

root =tk.Tk()               #練習１
root.geometry("300x500")

entry=tk.Entry(root,width=10,font=("Times New Roman",40),justify="right")#練習４

entry.grid(row=0, column=0, columnspan=3)


r, c = 1, 0
for i, num in enumerate(range(9,-1, -1), 1):  #練習２
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text="+", font=("", 30), width=4, height=2)
btn.bind("<1>", click2)
btn.grid(row=4, column=1)

root.mainloop()