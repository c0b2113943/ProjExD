import random
import sys

import pygame as pg


def main ():           #ゲーム画面
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("逃げろ！こうかとん")
    
    bg = pg.image.load("ex04/pg_bg.jpg") 
    bg_rect=bg.get_rect()  

    tori = pg.image.load("fig/0.png")       #こうかとん
    toriX,toriY=900,400 
    tori=pg.transform.rotozoom(tori,0,2.0)
    tori_rect=tori.get_rect()
    tori_rect.center=(toriX,toriY)

    draw_sfc=pg.Surface((20,20))         #爆弾
    drawX=random.randint(0,1600)
    drawY=random.randint(0,900)
    draw_sfc.set_colorkey("black")
    draw_rect=pg.draw.circle(draw_sfc,(255,0,0),(10,10),10)
    draw_rect.center=(drawX,drawY)
    vx=vy=1
   
    while True:
        scrn_sfc.blit(bg, bg_rect)
        scrn_sfc.blit(tori,tori_rect)
        scrn_sfc.blit(draw_sfc,draw_rect)

    
        pg.display.update()
        pg.time.Clock().tick(10000)

        draw_rect.move_ip(vx,vy)
        if draw_rect.left<0 or draw_rect.right>1600:
            vx=-vx
        if draw_rect.top<0 or draw_rect.bottom>900:
            vy=-vy    

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            if tori_rect.left>0:
                tori_rect.move_ip(-1,0)
        if pressed[pg.K_RIGHT]:
            if tori_rect.right<1600:
                tori_rect.move_ip(1,0)
        if pressed[pg.K_UP]:
            if tori_rect.top>0:
                tori_rect.move_ip(0,-1)
        if pressed[pg.K_DOWN]:
            if tori_rect.bottom<900:
                tori_rect.move_ip(0,1)
        
        hanntei=tori_rect.colliderect(draw_rect)
        if hanntei:
            return


if __name__=="__main__":
    main()