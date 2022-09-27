import random

num_all=10
num_ch=2
chm=[]
matigae=2
def shutudai():
    global chm
    alphabet = [chr(i+65) for i in range(26)]
    all = random.sample(alphabet, num_all)
    print("対象文字：", end="")
    for c in sorted(all): 
        print(c, end=" ")
    print()
    ch=random.sample(all,num_ch)
    print("表示文字：", end="")
    for i in all:
        if i not in ch:
            print(i,end=" ")
    print()
    print("欠損文字：", end=" ")
    chm=[]
    for i in  ch:
        print(i,end=" ")
        chm.append(i)


def kaitou ():
    global chm
    num=(input("欠損文字数を答えてください："))
    num=int(num)
    if num!= num_ch:
        print("残念")
    else:
        print("正解！　では何が欠損していますか？一文字ずつ回答してください")
        for i in range (num_ch):
            a=input(f"{i+1}文字目を入力して下い")
            if a not in chm:
                print("残念")
                break
            else:
                print("正解")
                chm.remove(a)
            

shutudai()
print()
kaitou ()