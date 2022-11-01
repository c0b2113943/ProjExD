import random
import sys

import pygame as pg


class Screen:       #スクリーン用
    def __init__(self,title,wh,bgfile):
        pg.display.set_caption(title)  
        self.scrn_sfc=pg.display.set_mode(wh)       #スクリーン用sfc
        self.scrn_rect=self.scrn_sfc.get_rect()     #スクリーン用Rect
        self.bg_sfc =pg.image.load(bgfile)     #背景Sfc
        self.bg_rect=self.bg_sfc.get_rect()         #背景Rect 
    
    def blit(self):
        self.scrn_sfc.blit(self.bg_sfc,self.bg_rect)
        return self.scrn_sfc
            

class Bird:             #こうかとん用
    key_delta = {
    pg.K_UP:    [0, -2],
    pg.K_DOWN:  [0, +2],
    pg.K_LEFT:  [-2, 0],
    pg.K_RIGHT: [+2, 0],
    }
    tori=["fig/6.png","fig/6-1.png"]

    def __init__(self,filename,bairitu,syokiiti):
        self.gazou_sfc=pg.image.load(filename)
        self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 0, bairitu)
        self.gazou_rect=self.gazou_sfc.get_rect()
        self.gazou_rect.center=(syokiiti)
    
    def blit(self,sc):
        sc.blit(self.gazou_sfc,self.gazou_rect)
    
    def update(self,sc):
        global z
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.gazou_rect.centerx += delta[0]
                self.gazou_rect.centery += delta[1] 
                if check_bound(self.gazou_rect,sc.get_rect()) != (+1, +1):
                    self.gazou_rect.centerx -= delta[0]
                    self.gazou_rect.centery -= delta[1]  
        self.gazou_sfc=pg.image.load(Bird.tori[z])
        self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 0, 2.0)
        sc.blit(self.gazou_sfc,self.gazou_rect)
        
        
class Bomb:         #爆弾用
    def __init__(self,iro,hannkei,sokudo,sc):
        self.bakudan_sfc=pg.Surface((hannkei*2,hannkei*2))
        drawX=random.randint(sc.scrn_rect.left,sc.scrn_rect.right)
        drawY=random.randint(sc.scrn_rect.top,sc.scrn_rect.bottom)
        self.bakudan_sfc.set_colorkey("black")
        self.bakudan_rect=pg.draw.circle(self.bakudan_sfc,iro,(hannkei,hannkei),hannkei)
        self.bakudan_rect.center=(drawX,drawY)
        self.vx,self.vy=sokudo

    def blit(self,sc):
        sc.blit(self.bakudan_sfc,self.bakudan_rect)
    
    def update(self,sc):
        self.bakudan_rect.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.bakudan_rect, sc.get_rect())
        self.vx *= yoko
        self.vy *= tate
        sc.blit(self.bakudan_sfc,self.bakudan_rect)

class Ken:    #剣用
    global enemy,enemy2
    def __init__(self,bairitu,bird):
        self.gazou_sfc=pg.image.load("ex05/1.jpg")
        self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 0, bairitu)
        self.gazou_rect=self.gazou_sfc.get_rect()
        self.gazou_rect.center=((bird.gazou_rect.centerx-90,bird.gazou_rect.centery-50))    #こうかとんの位置を使って更新
        self.bird1=bird

    def blit(self,sc):
        sc.blit(self.gazou_sfc,self.gazou_rect)
    
    def update(self,sc,bird):
        global x,y,z
        #key_states = pg.key.get_pressed()
        for even in pg.event.get():
            if even.type == pg.KEYDOWN and even.key==pg.K_SPACE:
                y=-50
                if z==0:
                    self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 90, 1)    #スペースキーで攻撃　左向き　　スイングの向きが違うため
                else:
                    self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, -90, 1)   #スペースキーで攻撃　右向き　

                ans=self.gazou_rect.collidelistall(enemy)
                for i in ans:                                                   #攻撃した際に爆弾と剣の当たり判定を取る 
                    enemy2[i].set_alpha(0)
                    del enemy[i]
                    del enemy2[i]
            if even.type == pg.KEYUP and even.key==pg.K_SPACE:
                y=50
                if z==0:
                    self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, -90, 1)   #スペースキーを離したときで攻撃戻す　左向き　　スイングの向きが違うため
                else:
                    self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 90, 1)    #スペースキーを離したとき攻撃戻す　右向き　　スイングの向きが違うため
            key_states = pg.key.get_pressed()
            if key_states[pg.K_RIGHT]and z!=1:
                x=-90
                z=1
                self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, -90, 1)       #右キーが押されたとき剣を右向きにする
            if key_states[pg.K_LEFT]and z!=0:
                x=90
                z=0
                self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 90, 1)
        self.gazou_rect.center=((bird.gazou_rect.centerx-x,bird.gazou_rect.centery-y))
        sc.blit(self.gazou_sfc,self.gazou_rect)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct:こうかとんrct,または,爆弾rct
    scr_rct:スクリーンrct
    領域内：+1/領域外:-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    pg.init()
    global enemy ,enemy2
    sc=Screen("負けるな！こうかとん",(1600,900),"ex05\pg_bg.jpg")
    bird=Bird("fig/6.png",2.0,(900,400))
    ken=Ken(0.5,bird)

    bom=Bomb((255,0,0),25,(1,1),sc)
    bom2=Bomb((255,0,0),25,(1,1),sc)
    bom3=Bomb((255,0,0),25,(1,1),sc)
    enemy.append(bom.bakudan_rect)
    enemy2.append(bom.bakudan_sfc)
    enemy.append(bom2.bakudan_rect)
    enemy2.append(bom2.bakudan_sfc)
    enemy.append(bom3.bakudan_rect)
    enemy2.append(bom3.bakudan_sfc)
    clock = pg.time.Clock() 
    pg.time.set_timer(30,5000)
    
    while True:
        nsc=sc.blit()
        bird.blit(nsc)
        bird.update(nsc)
        bom.blit(nsc)
        bom.update(nsc)
        bom2.blit(nsc)
        bom2.update(nsc)
        bom3.blit(nsc)
        bom3.update(nsc)
        ken.blit(nsc)
        ken.update(nsc,bird)

        # for event in pg.event.get():
        #     if event.type == 30:
        #         bom4=Bomb((255,0,0),25,(1,1),sc)
        #         enemy.append(bom4.bakudan_rect)
        #         enemy2.append(bom4.bakudan_sfc)
        
        if bird.gazou_rect.collidelist(enemy)!=-1:
            return
        key_states = pg.key.get_pressed()           #なぜかQite出来なかったのでエスケイプキーで終了
        if key_states[pg.K_ESCAPE]:
            return

        pg.display.update() 
        clock.tick(1000)
       
if __name__ == "__main__":
    enemy=[]
    enemy2=[]
    x,y,z=90,50,0
    pg.init() # 初期化
    main()
    pg.quit() # 初期化の解除
    sys.exit()
