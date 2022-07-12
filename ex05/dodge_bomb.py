import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import numpy as np
import IPython
from pygame import mixer


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode((wh))#スクリーンの大きさ
        self.rct=self.sfc.get_rect()
        self.bgimg_sfc=pg.image.load(image)#画像を取得
        self.bgimg_rct=self.bgimg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgimg_sfc, self.bgimg_rct)#表示


class Bird:
    def __init__(self, image:str, size:float, xy):
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
        if key_states[pg.K_LEFT]:
            self.rct.centerx-=1#ボタンが押されたときの反応
        if key_states[pg.K_RIGHT]:
            self.rct.centerx+=1#ボタンが押されたときの反応
        if check_bound(self.rct, scr.rct)!=(1,1) :#領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery+=1#ボタンが押されたときの反応
            if key_states[pg.K_DOWN]:
                self.rct.centery-=1#ボタンが押されたときの反応
            if key_states[pg.K_LEFT]:
                self.rct.centerx+=1#ボタンが押されたときの反応
            if key_states[pg.K_RIGHT]:
                self.rct.centerx-=1#ボタンが押されたときの反応
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)#出現位置のx座標をランダムに
        self.rct.centery = random.randint(0, scr.rct.height)#出現位置のy座標をランダムに
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)#blit

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)#判定
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


class End:
    def __init__(self):
        mixer.init()#初期化
        mixer.music.load("fig/poka.mp3")#音声ファイルの呼び出し
        mixer.music.play(1)#再生回数


class Bgm:
    def __init__(self):
        mixer.init()        #初期化
        mixer.music.load("fig/BGM.mp3") #BGMの音声ファイルの呼び出し
        mixer.music.play(1000) #再生回数


class Enemy:
    def __init__(self, image,xy, vxy, size,scr: Screen):
        self.sfc=pg.image.load(image)#画像を取得
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#２倍にズーム
        self.rct=self.sfc.get_rect()
        self.rct.center=xy #位置を設定
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct) #判定
        self.vx *= yoko #向きを確認
        self.vy *= tate#向きを確認
        self.blit(scr)  


class Word:
    def __init__(self ,title, text):
        tkm.showwarning(title,text)#終了時のテキストを表示


def main():#メイン関数
    clock=pg.time.Clock()
    Bgm()

#練習２　背景
    scr= Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")

#練習３　こうかとん
    num=random.randint(0,9)#こうかとんをランダムで表示するためのランダム関数
    koukatonx=random.randint(200,1400)#こうかとんの初期位置のx座標をランダムに表示するためのランダム関数
    koukatony=random.randint(200,700)#こうかとんの初期位置のｙ座標をランダムに表示するためのランダム関数
    kkt=Bird(f"fig/{num}.png",2.0,(koukatonx,koukatony))

#練習５爆弾
    bkd = Bomb((255,0,0), 10, (+4,+4), scr)
    enemyx=random.randint(200,1400)#敵の初期位置のx座標をランダムに表示するためのランダム関数
    enemyy=random.randint(200,700)#敵の初期位置のy座標をランダムに表示するためのランダム関数
    teki = Enemy("fig/enemy1.png",(enemyx,enemyy),(+4,+4),0.25,scr)

    while True:
        scr.blit()
        
        for event in pg.event.get():
            if event.type==pg.QUIT: return
            
        kkt.update(scr) #kktのupdateを起動
        bkd.update(scr) #bkdのupdateを起動
        teki.update(scr)#tekiのupdateを起動

        if kkt.rct.colliderect(teki.rct):
            End()#Endクラスを起動
            Word("ゲームクリア","敵はこうかとんによって倒された")#ゲームクリア文の表示
            return
        if kkt.rct.colliderect(bkd.rct):
            End()#Endクラスを起動
            Word("ゲームオーバー","残念！また挑戦してね")#ゲームオーバー文の表示
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1]rct:こうかとん or 爆弾のrct
    [2]scr_rct:スクリーンのRect
    '''
    yoko, tate= +1, +1
    if rct.left < scr_rct.left or scr_rct.right<rct.right: yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom<rct.bottom: tate = -1 #領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()