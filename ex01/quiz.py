import random

def main():
    question_number=random.randint(0,3)
    shutudai(question_number)
    kaito(question_number)

def shutudai(x):
    q1="サザエの旦那の名前は？"
    q2="カツオの妹の名前は？"
    q3="タラオはカツオから見てどんな関係？"
    q=[q1,q2,q3]
    question=q.pop(x)
    print(question)
def kaito(x):
    a1=["マスオ","ますお"]
    a2=["ワカメ","わかめ"]
    a3=["甥","おい","甥っ子","おいっこ"]
    a=[a1,a2,a3]
    answer=input("答えるんだ:")
    correct_answer=a.pop(x)
    result = answer in correct_answer
    if result==True:
        print("正解")
    else:
        print("出直してこい")

main()