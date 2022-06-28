import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random

def key_down(event):
    global key #グローバル宣言
    key=event.keysym
    root.after(100,main_proc)
    #print(f"{key}が押されました") #テスト用

def key_up(event):
    global key #グローバル宣言
    key=""
    root.after(100,main_proc)

def main_proc():
    global mx,my,cx,cy #グローバル宣言
    delta={"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}#入力されたキーによる移動方向
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0: #もし移動先が壁なら
            #tkm.showwarning("警告","壁に当たってるで")
            my,mx=my+delta[key][1], mx+delta[key][0]
    except:  #方向キー以外が入力された場合の例外処理                            
        print("方向キーを押してください") #方向キーが押されていない間の案内文
        pass
    cx, cy=mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    root.after(10000,main_proc)

if __name__ == "__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん") #タイトルを設定
    canvas=tk.Canvas(root, width=1500, height=1000, bg="red")#キャンバスを作成
    
    maze_bg=mm.make_maze(15,9)
    mm.show_maze(canvas, maze_bg)
    a=random.randint(0,9)
    tori = tk.PhotoImage(file=f"fig/{a}.png") #fig/4.pngから画像を持ってくる
    mx,my=1,1
    cx, cy=mx*100+50, my*100+50 #画像の配置位置を設定
    canvas.create_image(cx, cy, image=tori, tag="tori") #画像を配置
    canvas.pack() #パック
    label = tk.Label(root,text="escape from maze",font=("Times New Roman",20),fg="white",bg="blue") #色を変更したラベルを追加
    label.place(x=0, y=900)#ラベルの位置を変更

    key=""
    root.bind("<KeyPress>", key_down) #バインド
    root.bind("<KeyRelease>", key_up) #バインド

    main_proc()

    root.mainloop()
