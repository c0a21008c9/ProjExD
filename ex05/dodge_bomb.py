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
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)#２倍にズーム
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
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        # 練習5
        self.blit(scr)          


def main():
    clock=pg.time.Clock()

    mixer.init()        #初期化
    mixer.music.load("fig/BGM.mp3") #BGMの音声ファイルの呼び出し
    mixer.music.play(1000) #再生回数

#練習２　背景
    #pg.display.set_caption("逃げろ！こうかとん")
    #screen_sfc=pg.display.set_mode((1600,900))#スクリーンの大きさ
    #screen_rct=screen_sfc.get_rect()
    #bgimg_sfc=pg.image.load("fig/pg_bg.jpg")#画像を取得
    #bgimg_rct=bgimg_sfc.get_rect()
    #screen_sfc.blit(bgimg_sfc, bgimg_rct)#表示
    scr= Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

#練習３　こうかとん
    num=random.randint(0,9)#こうかとんをランダムで表示するためのランダム関数
    #kking_sfc=pg.image.load(f"fig/{num}.png")#画像を取得
    #kkimg_sfc=pg.transform.rotozoom(kking_sfc, 0, 2.0)#２倍にズーム
    #kking_rct=kking_sfc.get_rect()
    koukatonx=random.randint(200,1400)#こうかとんの初期位置のx座標をランダムに表示するためのランダム関数
    koukatony=random.randint(200,700)#こうかとんの初期位置のｙ座標をランダムに表示するためのランダム関数
    #kking_rct.center=koukatonx, koukatony #位置を設定
    #screen_sfc.blit(kkimg_sfc,kking_rct)#表示
    kkt=Bird(f"fig/{num}.png",2.0,(koukatonx,koukatony))

#練習５爆弾
    #boming_sfc=pg.Surface((20,20))
    #boming_sfc.set_colorkey((0,0,0))#余計な部分を削除
    #pg.draw.circle(boming_sfc ,(255, 0, 0),(10,10),10)#描写
    #boming_rct=boming_sfc.get_rect()
    #boming_rct.centerx = random.randint(0, screen_rct.width)#出現位置のｘ座標をランダムに
    #boming_rct.centery = random.randint(0, screen_rct.height)#出現位置のy座標をランダムに
    #vx, vy= +1, +1
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)

    while True:
        scr.blit()
        
#練習２
        for event in pg.event.get():
            if event.type==pg.QUIT: return
            
#練習４ボタンが押された時の反応
        #key_states=pg.key.get_pressed()
        #if key_states[pg.K_UP] == True:kking_rct.centery-=1#ボタンが押されたときの反応
        #if key_states[pg.K_DOWN]==True:kking_rct.centery+=1#ボタンが押されたときの反応
        #if key_states[pg.K_LEFT]==True:kking_rct.centerx-=1#ボタンが押されたときの反応
        #if key_states[pg.K_RIGHT]==True:kking_rct.centerx+=1#ボタンが押されたときの反応
        #if check_bound(kking_rct, screen_rct)!=(1,1) :#領域外だったら
        #    if key_states[pg.K_UP] == True:kking_rct.centery+=1#ボタンが押されたときの反応
        #    if key_states[pg.K_DOWN]==True:kking_rct.centery-=1#ボタンが押されたときの反応
        #    if key_states[pg.K_LEFT]==True:kking_rct.centerx+=1#ボタンが押されたときの反応
        #    if key_states[pg.K_RIGHT]==True:kking_rct.centerx-=1#ボタンが押されたときの反応
        #screen_sfc.blit(kkimg_sfc,kking_rct)
        kkt.update(scr)
        bkd.update(scr)
#練習６爆弾の移動
        #boming_rct.move_ip(vx,vy)

#練習５スクリーンの表示
        #screen_sfc.blit(boming_sfc, boming_rct)


        #yoko, tate= check_bound(boming_rct, screen_rct)
        #vx*=yoko
        #vy*=tate

#練習8　ゲームを終了させる
        #if kking_rct.colliderect(boming_rct):
        if kkt.rct.colliderect(bkd.rct):
            game_over()
            tkm.showwarning("ゲームオーバー","残念！また挑戦してね")#ゲームオーバー文の表示
            return

        pg.display.update()
        clock.tick(1000)

def game_over(): #ゲームオーバーの際の効果音の追加
    mixer.init()#初期化
    mixer.music.load("fig/poka.mp3")#音声ファイルの呼び出し
    mixer.music.play(1)#再生回数

    #音声自作の際に利用
    #rate=4800
    #d=1.0
    #t=np.linspace(0.,d,int(rate*d))
    #x=np.sin(2.0*np.pi*440.0*t)
    #IPython.display.Audio(x, rate=rate, autoplay=True)

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