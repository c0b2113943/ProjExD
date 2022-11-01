import random
import sys

import pygame as pg


class Screen:
    
    def __init__(self,title,wh,bgfile):
        pg.display.set_caption(title)  
        self.scrn_sfc=pg.display.set_mode(wh)       #スクリーン用sfc
        self.scrn_rect=self.scrn_sfc.get_rect()     #スクリーン用Rect
        self.bg_sfc =pg.image.load(bgfile)     #背景Sfc
        self.bg_rect=self.bg_sfc.get_rect()         #背景Rect 
  

    def blit(self):
        self.scrn_sfc.blit(self.bg_sfc,self.bg_rect)
        return self.scrn_sfc
            
class Bird:
    key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
    }

    def __init__(self,filename,bairitu,syokiiti):
        self.gazou_sfc=pg.image.load(filename)
        self.gazou_sfc= pg.transform.rotozoom(self.gazou_sfc, 0, bairitu)
        self.gazou_rect=self.gazou_sfc.get_rect()
        self.gazou_rect.center=(syokiiti)
    
    def blit(self,sc):
        sc.blit(self.gazou_sfc,self.gazou_rect)
    
    def update(self,sc):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.gazou_rect.centerx += delta[0]
                self.gazou_rect.centery += delta[1] 
                if check_bound(self.gazou_rect,sc.get_rect()) != (+1, +1):
                    self.gazou_rect.centerx -= delta[0]
                    self.gazou_rect.centery -= delta[1]  
        sc.blit(self.gazou_sfc,self.gazou_rect)

class Bomb:
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
    sc=Screen("逃げろこうかとん",(1600,900),"ex05\pg_bg.jpg")
    bird=Bird("fig/6.png",2.0,(900,400))
    bom=Bomb((255,0,0),25,(1,1),sc)
    

    clock = pg.time.Clock() 

    while True:
        nsc=sc.blit()
        bird.blit(nsc)
        bird.update(nsc)
        bom.blit(nsc)
        bom.update(nsc)
       
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
        

        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
