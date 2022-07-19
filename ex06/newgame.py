import pygame as pg
import sys
import random
import tkinter.messagebox as tkm
from pygame import mixer

count1,count2=0,0

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode((wh))#スクリーンの大きさ
        self.rct=self.sfc.get_rect()
        self.bgimg_sfc=pg.image.load(image)#画像を取得
        self.bgimg_rct=self.bgimg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgimg_sfc, self.bgimg_rct)#表示


class Line1:
    def __init__(self ,image,size,xy):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=xy #位置を設定

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):
        key_states=pg.key.get_pressed()
        if key_states[pg.K_w]:
            self.rct.centery-=1#ボタンが押されたときの反応
        if key_states[pg.K_s]:
            self.rct.centery+=1#ボタンが押されたときの反応
        if check_bound(self.rct, scr.rct)!=(1,1) :#領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery+=1#ボタンが押されたときの反応
            if key_states[pg.K_DOWN]:
                self.rct.centery-=1#ボタンが押されたときの反応
        self.blit(scr)


class Line2:
    def __init__(self ,image,size,xy):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=xy #位置を設定

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr: Screen):
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]:
            self.rct.centery-=1#ボタンが押されたときの反応
        if key_states[pg.K_DOWN]:
            self.rct.centery+=1#ボタンが押されたときの反応
        if check_bound(self.rct, scr.rct)!=(1,1) :#領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery+=1#ボタンが押されたときの反応
            if key_states[pg.K_DOWN]:
                self.rct.centery-=1#ボタンが押されたときの反応

        self.blit(scr)


class Ball:
    def __init__(self, image, vx,vy, scr: Screen):
        self.sfc = pg.image.load(image) # Surface
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.5)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 800#出現位置のx座標を中心に
        self.rct.centery = 450#出現位置のy座標を中心に
        self.vx, self.vy = vx, vy# 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)#blit

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)#判定
        self.vx *= yoko#反転
        self.vy *= tate#反転
        self.blit(scr)


class Obstacle:
    def __init__(self,image):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.25)#1/4倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=random.randint(500,1100),random.randint(100,800) #位置を設定

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)


class End:
    def __init__(self):
        mixer.init()#初期化
        mixer.music.load("fig/poka.mp3")#音声ファイルの呼び出し
        mixer.music.play(1)#再生回数


class Bgm:
    def __init__(self):
        mixer.init()        #初期化
        pg.mixer.music.set_volume(0.1)
        mixer.music.load("fig/BGM.mp3") #BGMの音声ファイルの呼び出し
        mixer.music.play(-1) #再生回数


class Word:
    def __init__(self ,title, text):
        tkm.showwarning(title,text)#終了時のテキストを表示

#メイン関数
def main():
    clock=pg.time.Clock()
    Bgm()

#背景
    scr= Screen("エアホッケー", (1600,900), "fig/bg.jpg")

#キーパー
    kpr=Line1(f"fig/line1.png",0.75,(50,450))
    kpr2=Line2(f"fig/line2.png",0.75,(1550,450))

#障害物
    obs=[]
    for i in range(3): #障害物を３つ生成
        obs.append(Obstacle("fig/障害物.png"))

#ボール
    ball = Ball("fig/ball.png", +4,+3, scr)

    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            
        kpr.update(scr) #kprのupdateを起動
        kpr2.update(scr) #kpr2のupdateを起動
        ball.update(scr) #ballのupdateを起動
        for i in obs:
            i.blit(scr)
            if i.rct.colliderect(ball.rct):
                ball.vx*=-1
                sound1=mixer.Sound("fig/反射音.mp3")#音声ファイルの呼び出し
                sound1.play(1)#再生回数

        if kpr.rct.colliderect(ball.rct):
            ball.vx*=-1
            sound1=mixer.Sound("fig/反射音.mp3")#音声ファイルの呼び出し
            sound1.play(1)#再生回数
        if kpr2.rct.colliderect(ball.rct):
            ball.vx*=-1
            sound2=mixer.Sound("fig/反射音.mp3")#音声ファイルの呼び出し
            sound2.play(1)#再生回数

        font = pg.font.Font(None,100)
        text = font.render(f"{count1}:{count2}", True, (255,255,255))#得点を表示
        scr.sfc.blit(text, [750, 50])#得点を表示

        if count1>=5:
            End()#Endクラスを起動
            Word("ゲームセット","プレイヤー2の勝利!")#ゲームセット文の表示
            return
        if count2>=5:
            End()#Endクラスを起動
            Word("ゲームセット","プレイヤー1の勝利!")#ゲームセット文の表示
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):#壁判定
    global count1, count2
    yoko, tate= +1, +1
    if rct.left < scr_rct.left:
        yoko = -1#領域外
        count1+=1#得点を加算
    if scr_rct.right<rct.right:
        yoko = -1 #領域外
        count2+=1#得点を加算
    if rct.top < scr_rct.top or scr_rct.bottom<rct.bottom: tate = -1 #領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()