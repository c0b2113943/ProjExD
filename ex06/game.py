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
            

class Bird:           #こうかとん用
    key_delta = {
    pg.K_UP:    [0, -5],
    pg.K_DOWN:  [0, +5],
    pg.K_LEFT:  [-5, 0],
    pg.K_RIGHT: [+5, 0],
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
        global z,tim
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.gazou_rect.centerx += delta[0]
                self.gazou_rect.centery += delta[1] 
                if check_bound(self.gazou_rect,sc.get_rect()) != (+1, +1):
                    self.gazou_rect.centerx -= delta[0]
                    self.gazou_rect.centery -= delta[1] 
            if key_states[pg.K_SPACE]and tim % 40==0:
                set_bullet(self.gazou_rect.centerx,self.gazou_rect.centery)
               

def set_bullet(px,py):#弾のスタンバイ
    global bull_n
    bull_f[bull_n] = True
    bull_x[bull_n] = px-16
    bull_y[bull_n] = py-32
    bull_n = (bull_n+1)%10
        

def move_bullet(screen):#弾を飛ばす
    global list2
    for i in range(10):
        if bull_f[i] == True:
            bull_y[i] = bull_y[i] -10
            sc=screen.blit(img_weapon,[bull_x[i],bull_y[i]])
            list2[i]=sc
            if bull_y[i] < 0:
                bull_f[i] = False
                list2.pop(i)
        

class Bomb:         #爆弾用
    def __init__(self,iro,hannkei,sokudo,sc):
        self.bakudan_sfc=pg.Surface((hannkei*2,hannkei*2))
        drawX=random.randint(sc.scrn_rect.left,sc.scrn_rect.right)
        drawY=30
        self.bakudan_sfc.set_colorkey("black")
        self.bakudan_rect=pg.draw.circle(self.bakudan_sfc,iro,(hannkei,hannkei),hannkei)
        self.bakudan_rect.center=(drawX,drawY)
        self.vx,self.vy=sokudo

    def blit(self,sc):
        if self.bakudan_rect.bottom<950:
            sc.blit(self.bakudan_sfc,self.bakudan_rect)
    
    def update(self,sc):
        self.bakudan_rect.move_ip(self.vx, self.vy)
        yoko, tate = check_bound2(self.bakudan_rect, sc.get_rect())
        self.vx *= yoko
        self.vy *= tate
             




def check_bound2(obj_rct, scr_rct):#爆弾用　下が開いている壁
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top : 
        tate = -1
    return yoko, tate        
        
def check_bound(obj_rct, scr_rct):#壁判定
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    global tim ,list2,counter,counter2,mod
    pg.init()
    sc=Screen("シューティングゲーム",(1600,900),"ex05\pg_bg.jpg")
    bird=Bird("fig/6.png",2.0,(900,400))
    bom=Bomb((255,0,0),25,(5,1),sc)
    enemy.append(bom.bakudan_rect)
    enemy2.append(bom.bakudan_sfc)
    BOM = pg.image.load("ex04/bakuhatsu.png")       #爆発
    font1=pg.font.Font(None,100)
    pg.time.set_timer(30,1000)
    clock = pg.time.Clock() 
    
    while True:
        nsc=sc.blit()
        tim+=1
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            if event.type==30:                #1秒ごとに爆弾を表示
                ans="fbom{counter}"
                ans=Bomb((255,0,0),25,(5,1),sc)
                enemy.append(ans.bakudan_rect)
                enemy2.append(ans.bakudan_sfc)
                counter2.append(ans)
                counter+=1    
        
        if bird.gazou_rect.collidelist(enemy)!=-1: #爆弾とこうかとんの当たり判定
            mod=2
            bom_rect=BOM.get_rect() 
            bom_rect.center=(bird.gazou_rect.centerx,bird.gazou_rect.centery)
            nsc.blit(BOM,bom_rect)
            pg.display.update()
            pg.time.delay(1500)
            return
        
        text1=font1.render(f"Score: {tim}", True, (0,0,255)) #スコアー表示
        nsc.blit(text1, [50, 50])
        bird.blit(nsc) #こうかとん
        bird.update(nsc)
        move_bullet(nsc)   #攻撃    
        bom.blit(nsc)     #爆弾
        bom.update(nsc)
        
        for i in counter2:  #一秒ごとの作成された爆弾の描画
            i.blit(nsc)
            i.update(nsc)
        
        for i in list2.values():        #攻撃と爆弾の当たり判定
            ans=i.collidelistall(enemy)
            for i in ans: 
                enemy2[i].set_alpha(0)
                del enemy[i]
                del enemy2[i] 
        pg.display.update() 
        clock.tick(100)

def main3 ():              #GameOver画面
    global mod,tim
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("Game Over")
    font=pg.font.Font(None,200)
    font1=pg.font.Font(None,100)

    while True:
        text=font.render("Game Over", True, (255,255,255))
        scrn_sfc.blit(text, [500, 400])
        text1=font1.render(f"Score: {tim}", True, (255,0,0))
        scrn_sfc.blit(text1, [500, 550])
        text1=font1.render("[r] : Rstert", True, (255,255,255))
        scrn_sfc.blit(text1, [500, 650])
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pressed = pg.key.get_pressed()
        if pressed[pg.K_r]:
            mod=1
            return
        if pressed[pg.K_e]:
            pg.quit()
            sys.exit()

if __name__ == "__main__":
    x,y,z=90,50,0
    img_weapon = pg.image.load("fig/6.png")
    bull_x =[0]*10
    bull_y =[0]*10
    bull_f =[False]*10  
    bull_n = 0
    enemy=[]
    enemy2=[] 
    tim=0
    list2={}
    counter=0
    counter2=[]
    mod=1
    while True:
        if mod==1:  #ゲーム画面
            main()
        if mod==2:  #GameOver画面
            main3()
    
