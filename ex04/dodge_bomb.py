import random
import sys

import pygame as pg


def main ():           #ゲーム画面
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("逃げろ！こうかとん")
    
    bg = pg.image.load("ex04/pg_bg.jpg") 
    bg_rect=bg.get_rect()  
   
    while True:
        scrn_sfc.blit(bg, bg_rect)
        pg.display.update()
        pg.time.Clock().tick(10000)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

if __name__=="__main__":
    main()