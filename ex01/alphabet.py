import random
import datetime
answer_number=10
luck_number=2
max_repeat=5
repeat=0
ans=[]
y=False
def main():
    st = datetime.datetime.now()
    while y==False:
        alphabets()
        que()
        if repeat == max_repeat:
            break
        else:
            continue
    ed = datetime.datetime.now()
    print(f"かかった時間:{(ed-st).seconds}秒")
def alphabets():
    global answer_number, luck_number, ans
    alp=[]
    for i in range(answer_number):
        number=random.randint(65,90)
        alphabet=chr(number)
        alp+=alphabet
    print("対象文字:")
    print(alp)
    n=answer_number
    for j in range(luck_number):
        n-=1
        luck=random.randint(0,n)
        ans+=alp.pop(luck)
    print("表示文字:")
    print(alp)
    #print(ans)

def que():
    global luck_number, ans, y, max_repeat, repeat
    x=int(input("欠損文字はいくつあるでしょうか？:"))
    if x==2:
        print("正解です。それでは、具体的に欠損文字を一つずつ入力してください")
        z=input("1つ目の文字を入力してください:")
        result = z in ans
        if result==True:
            z2=input("2つ目の文字を入力してください:")
            result2 = z2 in ans
            if result2==True:
                print("正解")
                y=True
        else:
            print("不正解です。またチャレンジしてください")
            repeat+=1
    else:
        print("不正解です。またチャレンジしてください")
        repeat+=1
if __name__ == "__main__":
    main()