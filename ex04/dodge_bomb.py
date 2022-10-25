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
   
    while True:
        scrn_sfc.blit(bg, bg_rect)
        scrn_sfc.blit(tori,tori_rect)

    
        pg.display.update()
        pg.time.Clock().tick(10000)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:
            tori_rect.move_ip(-1,0)
        if pressed[pg.K_RIGHT]:
            tori_rect.move_ip(1,0)
        if pressed[pg.K_UP]:
            tori_rect.move_ip(0,-1)
        if pressed[pg.K_DOWN]:
            tori_rect.move_ip(0,1)


if __name__=="__main__":
    main()