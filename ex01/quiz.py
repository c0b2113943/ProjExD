from tokenize import PseudoExtras
import random
qes=["サザエさんの旦那の名前は？","カツオの妹の名前は？","タラオ䛿カツオから見てどんな関係？"]
ans=[["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子"]]
ans1=0

def shutudai():
    a=random.randint(0,2)
    b=qes[a]
    global ans1
    ans1 =a
    return("問題："+b)
def kaito(aa):
    ans2="不正解"
    c=input("回答：")
    for i in ans[aa]:
        if i == c:
            ans2="正解"
            break
    return(ans2)

print(shutudai())
print(kaito(ans1))
