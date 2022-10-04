from cProfile import label
import tkinter as tk

root =tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label=tk.Label(root,
               text="ラベルを書いてみた件",
               font=("Ricty Diminished",20) 
               )
label.pack()

root.mainloop()