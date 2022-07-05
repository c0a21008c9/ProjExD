import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm
import numpy as np
import IPython
from pygame import mixer

def main():
    clock=pg.time.Clock()

    mixer.init()        #初期化
    mixer.music.load("fig/BGM.mp3") #BGMの音声ファイルの呼び出し
    mixer.music.play(1000) #再生回数

#練習２　背景
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc=pg.display.set_mode((1600,900))#スクリーンの大きさ
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg")#画像を取得
    bgimg_rct=bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)#表示

#練習３　こうかとん
    num=random.randint(0,9)#こうかとんをランダムで表示するためのランダム関数
    kking_sfc=pg.image.load(f"fig/{num}.png")#画像を取得
    kkimg_sfc=pg.transform.rotozoom(kking_sfc, 0, 2.0)#２倍にズーム
    kking_rct=kking_sfc.get_rect()
    koukatonx=random.randint(200,1400)#こうかとんの初期位置のx座標をランダムに表示するためのランダム関数
    koukatony=random.randint(200,700)#こうかとんの初期位置のｙ座標をランダムに表示するためのランダム関数
    kking_rct.center=koukatonx, koukatony #位置を設定
    screen_sfc.blit(kkimg_sfc,kking_rct)#表示
#練習５爆弾
    boming_sfc=pg.Surface((20,20))
    boming_sfc.set_colorkey((0,0,0))#余計な部分を削除
    pg.draw.circle(boming_sfc ,(255, 0, 0),(10,10),10)#描写
    boming_rct=boming_sfc.get_rect()
    boming_rct.centerx = random.randint(0, screen_rct.width)#出現位置のｘ座標をランダムに
    boming_rct.centery = random.randint(0, screen_rct.height)#出現位置のy座標をランダムに
    vx, vy= +1, +1


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        

        for event in pg.event.get():
            if event.type==pg.QUIT: return#終了判定
#練習４
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP] == True:kking_rct.centery-=1#ボタンが押されたときの反応
        if key_states[pg.K_DOWN]==True:kking_rct.centery+=1#ボタンが押されたときの反応
        if key_states[pg.K_LEFT]==True:kking_rct.centerx-=1#ボタンが押されたときの反応
        if key_states[pg.K_RIGHT]==True:kking_rct.centerx+=1#ボタンが押されたときの反応
        if check_bound(kking_rct, screen_rct)!=(1,1) :#領域外だったら
            if key_states[pg.K_UP] == True:kking_rct.centery+=1#ボタンが押されたときの反応
            if key_states[pg.K_DOWN]==True:kking_rct.centery-=1#ボタンが押されたときの反応
            if key_states[pg.K_LEFT]==True:kking_rct.centerx+=1#ボタンが押されたときの反応
            if key_states[pg.K_RIGHT]==True:kking_rct.centerx-=1#ボタンが押されたときの反応
        screen_sfc.blit(kkimg_sfc,kking_rct)

#練習６
        boming_rct.move_ip(vx,vy)

#練習５
        screen_sfc.blit(boming_sfc, boming_rct)

#練習 7
        yoko, tate= check_bound(boming_rct, screen_rct)
        vx*=yoko
        vy*=tate

#練習8
        if kking_rct.colliderect(boming_rct):
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