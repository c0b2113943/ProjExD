from ast import Delete
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

def click_eq(event):  #7
    get=entry.get()
    get=get.replace("×","*")   #掛け算、割り算対応
    get=get.replace("÷","/")
    ans=round(eval(get),10)
    entry.delete(0,tk.END)
    entry.insert(tk.END, ans)

def click_del(event):         #消去
    entry.delete(0,tk.END)
    

def click_del1(event):     #一文字消去
    get=entry.get()
    ans=get[:-1]
    entry.delete(0,tk.END)
    entry.insert(tk.END, ans)

def click_x(event):     #二乗
    get=entry.get()
    ans=int(get)
    ans=ans*ans
    entry.delete(0,tk.END)
    entry.insert(tk.END, ans)
    
   
    
    

root =tk.Tk()               #練習１
root.geometry("400x620")

entry=tk.Entry(root,width=14,font=("Times New Roman",40),justify="right")#練習４
entry.grid(row=0, column=0, columnspan=4)


r, c = 1, 0
for i, num in enumerate(range(9,-1, -1), 1):  #練習２
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

btn = tk.Button(root, text="+", font=("", 30), width=4, height=2)#6
btn.bind("<1>", click2)
btn.grid(row=4, column=3)
btn = tk.Button(root, text="-", font=("", 30), width=4, height=2)#引き算
btn.bind("<1>", click2)
btn.grid(row=3, column=3)
btn = tk.Button(root, text="×", font=("", 30), width=4, height=2)#掛け算
btn.bind("<1>", click2)
btn.grid(row=1, column=3)
btn = tk.Button(root, text="÷", font=("", 30), width=4, height=2)#割り算
btn.bind("<1>", click2)
btn.grid(row=2, column=3)
btn = tk.Button(root, text=".", font=("", 30), width=4, height=2)#小数
btn.bind("<1>", click2)
btn.grid(row=4, column=1)

btn = tk.Button(root, text="AC", font=("", 30), width=4, height=2,bg="red")#全消去
btn.bind("<1>", click_del)
btn.grid(row=5, column=2)

btn = tk.Button(root, text="C", font=("", 30), width=4, height=2,bg="#ffffcc")#一文字消去
btn.bind("<1>", click_del1)
btn.grid(row=5, column=3)


btn = tk.Button(root, text="=", font=("", 30), width=4, height=2)#7
btn.bind("<1>", click_eq)
btn.grid(row=4, column=2)

btn = tk.Button(root, text="x^2", font=("", 30), width=4, height=2)# 二乗
btn.bind("<1>", click_x)
btn.grid(row=5, column=1)

root.mainloop()