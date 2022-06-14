import random

def main():
    mondai_bangou=random.randint(0,3)
    shutudai(mondai_bangou)
    kaito(mondai_bangou)

def shutudai(x):
    q1="サザエの旦那の名前は？"
    q2="カツオの妹の名前は？"
    q3="タラオはカツオから見てどんな関係？"
    q=[q1,q2,q3]
    mondai=q.pop(x)
    print(mondai)
def kaito(x):
    a1=["マスオ","ますお"]
    a2=["ワカメ","わかめ"]
    a3=["甥","おい","甥っ子","おいっこ"]
    a=[a1,a2,a3]
    kaitou=input("答えるんだ:")
    kotae=a.pop(x)
    result = kaitou in kotae
    if result==True:
        print("正解")
    else:
        print("出直してこい")

main()