import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key,jid #グローバル宣言
    key=event.keysym
    jid = root.after(100,main_proc)
    #print(f"{key}が押されました") #テスト用

def key_up(event):
    global key #グローバル宣言
    key=""
    root.after(100,main_proc)

def main_proc():
    global jid,mx,my,cx,cy #グローバル宣言
    delta={"Up":[0,-1],"Down":[0,+1],"Left":[-1,0],"Right":[+1,0]}#入力されたキーによる移動方向
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0: #もし移動先が壁なら
            my,mx=my+delta[key][1], mx+delta[key][0]
    except:  #方向キー以外が入力された場合の例外処理                            
        pass
    cx, cy=mx*100+50, my*100+50
    canvas.coords("tori",cx,cy)
    jid = root.after(10000,main_proc)

if __name__ == "__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん") #タイトルを設定

    canvas=tk.Canvas(root, width=1500, height=900, bg="black")#キャンバスを作成
    
    maze_bg=mm.make_maze(15,9)
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/6.png") #fig/6.pngから画像を持ってくる
    mx,my=1,1
    cx, cy=mx*100+50, my*100+50 #画像の配置位置を設定
    canvas.create_image(cx, cy, image=tori, tag="tori") #画像を配置
    canvas.pack() #パック

    key=""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()
