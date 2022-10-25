import random
import sys

import pygame as pg

png=["fig/0.png","fig/1.png","fig/2.png"]
toriping=0

def main (): 
    global toriping          #ゲーム画面
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("逃げろ！こうかとん")
    
    bg = pg.image.load("ex04/pg_bg.jpg") #背景
    bg_rect=bg.get_rect()  
    toripng=png[toriping]

    #tori = pg.image.load("fig/0.png")       #こうかとん
    tori = pg.image.load(toripng)       #キャラクター選択画面で選ばれたこうかとんを表示する
    toriX,toriY=900,400 
    tori=pg.transform.rotozoom(tori,0,2.0)
    tori_rect=tori.get_rect()
    tori_rect.center=(toriX,toriY)

    draw_sfc=pg.Surface((50,50))         #爆弾
    drawX=random.randint(1,1600)
    drawY=random.randint(1,900)
    draw_sfc.set_colorkey("black")
    draw_rect=pg.draw.circle(draw_sfc,(255,0,0),(25,25),25)
    draw_rect.center=(drawX,drawY)
    vx=vy=1

    HP = pg.image.load("ex04\無題.jpg")       #HPバー
    HP_rect=HP.get_rect() 
    HP_rect.center=(toriX,toriY+80)

    HP2 = pg.image.load("ex04/1.png")       #HPの色がある部分
    HP2_rect=HP2.get_rect() 
    HP2_rect.center=(toriX-40,toriY+80)
    
    HP3_rect=HP2.get_rect() 
    HP3_rect.center=(toriX-20,toriY+80)
    
    HP4_rect=HP2.get_rect() 
    HP4_rect.center=(toriX,toriY+80)
    
    HP5_rect=HP2.get_rect() 
    HP5_rect.center=(toriX+20,toriY+80)
    
    HP6_rect=HP2.get_rect() 
    HP6_rect.center=(toriX+40,toriY+80)

    BOM = pg.image.load("ex04/bakuhatsu.png")       #爆発
    bom_rect=BOM.get_rect() 
    bom_rect.center=(toriX,toriY)

    
    HP3 = pg.image.load("ex04/1.png")  #判定用
    HP3.set_alpha(0)                    #判定用に透明なゲージを０以下の位置に置き、一定ダメージ時これに当たるまで移動するようにした。
    HP7_rect=HP2.get_rect()             #最終的に1/5残った形になる。
    HP7_rect.center=(toriX-60,toriY+80)
    HP8_rect=HP2.get_rect() 
    HP8_rect.center=(toriX-80,toriY+75)
    font1=pg.font.Font(None,40)
    damezi=0
   
    while True:
        global mod
        scrn_sfc.blit(bg, bg_rect)#背景
        if damezi>=500:                     #ダメージが500以上になったら表示
            scrn_sfc.blit(BOM,bom_rect)
        scrn_sfc.blit(tori,tori_rect)#鳥
        scrn_sfc.blit(draw_sfc,draw_rect)#爆弾
        scrn_sfc.blit(HP,HP_rect)       #HPバー
        scrn_sfc.blit(HP2,HP2_rect)     #HP色があるとこ
        scrn_sfc.blit(HP2,HP3_rect)     #HP色があるとこ
        scrn_sfc.blit(HP2,HP4_rect)     #HP色があるとこ
        scrn_sfc.blit(HP2,HP5_rect)     #HP色があるとこ
        scrn_sfc.blit(HP2,HP6_rect)     #HP色があるとこ
        scrn_sfc.blit(HP3,HP7_rect)     #HP色がないとこ
        text1=font1.render("HP", True, (0,0,0))
        scrn_sfc.blit(text1,HP8_rect)   #HP表示
        
       
    
        pg.display.update()
        pg.time.Clock().tick(10000)

        draw_rect.move_ip(vx,vy)
        if draw_rect.left<0 or draw_rect.right>1600:  #爆弾の壁判定
            vx=-vx
        if draw_rect.top<0 or draw_rect.bottom>900:   #爆弾の壁判定
            vy=-vy    

        for event in pg.event.get():    #タブを閉じたとき
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        pressed = pg.key.get_pressed()
        if pressed[pg.K_LEFT]:          #左が押されたとき
            if tori_rect.left>0:
                tori_rect.move_ip(-1,0)
                HP_rect.move_ip(-1,0)
                HP2_rect.move_ip(-1,0)
                HP3_rect.move_ip(-1,0)
                HP4_rect.move_ip(-1,0)
                HP5_rect.move_ip(-1,0)
                HP6_rect.move_ip(-1,0)
                HP7_rect.move_ip(-1,0)
                HP8_rect.move_ip(-1,0)
                bom_rect.move_ip(-1,0)
        
        if pressed[pg.K_RIGHT]:          #右が押されたとき
            if tori_rect.right<1600:
                tori_rect.move_ip(1,0)
                HP_rect.move_ip(1,0)
                HP2_rect.move_ip(1,0)
                HP3_rect.move_ip(1,0)
                HP4_rect.move_ip(1,0)
                HP5_rect.move_ip(1,0)
                HP6_rect.move_ip(1,0)
                HP7_rect.move_ip(1,0)
                HP8_rect.move_ip(1,0)
                bom_rect.move_ip(1,0)
        
        if pressed[pg.K_UP]:          #上が押されたとき
            if tori_rect.top>0:
                tori_rect.move_ip(0,-1)
                HP_rect.move_ip(0,-1)
                HP2_rect.move_ip(0,-1)
                HP3_rect.move_ip(0,-1)
                HP4_rect.move_ip(0,-1)
                HP5_rect.move_ip(0,-1)
                HP6_rect.move_ip(0,-1)
                HP7_rect.move_ip(0,-1)
                HP8_rect.move_ip(0,-1)
                bom_rect.move_ip(0,-1)

        if pressed[pg.K_DOWN]:          #下が押されたとき
            if tori_rect.bottom<855:
                tori_rect.move_ip(0,1)
                HP_rect.move_ip(0,1)
                HP2_rect.move_ip(0,1)
                HP3_rect.move_ip(0,1)
                HP4_rect.move_ip(0,1)
                HP5_rect.move_ip(0,1)
                HP6_rect.move_ip(0,1)
                HP7_rect.move_ip(0,1)
                HP8_rect.move_ip(0,1)
                bom_rect.move_ip(0,1)
        
        #hanntei=tori_rect.colliderect(draw_rect)#爆弾と鳥の当たり判定
        if tori_rect.colliderect(draw_rect):
            damezi+=1
        
        if damezi>=501:       #ダメージが501（約5回）当たったら処理を1.5秒停止し爆発している画面を見せている
            pg.time.delay(1500)
            mod=2
            return
        elif damezi>=500:       #ダメージが500（約5回）当たったらHPバーを無色にする
            HP2.set_alpha(0)
        elif damezi>=400:         #ダメージが400（約4回）当たったらHPバーを赤色にする     
            HP2.fill("red")
        elif damezi>=300:       #ダメージが300（約3回）当たったらHPバーを黄色にする
            HP2.fill("yellow")

        if damezi>=90 and HP6_rect.colliderect(HP7_rect)==False : #ダメージが90以上になったらHPゲージを減らす（残量約4／5　）
            HP6_rect.move_ip(-1,0)
        elif damezi>=200 and HP5_rect.colliderect(HP7_rect)==False:#ダメージが2000以上になったらHPゲージを減らす（約3／5　）
            HP5_rect.move_ip(-1,0)
        elif damezi>=300 and HP4_rect.colliderect(HP7_rect)==False:#ダメージが300以上になったらHPゲージを減らす（約2／5　）
            HP4_rect.move_ip(-1,0)
        elif damezi>=400 and HP3_rect.colliderect(HP7_rect)==False:#ダメージが300以上になったらHPゲージを減らす（約1／5　）
            HP3_rect.move_ip(-1,0)
        
        

def main2 ():               #スタート画面
    global mod ,toriping
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("初めてのPyGame")
    
    bg = pg.image.load("ex04/pg_bg.jpg") 
    bg_rect=bg.get_rect()  
    toripn=png[toriping]
    tori = pg.image.load(toripn)
    toriX,toriY=700,430 
    tori=pg.transform.rotozoom(tori,0,3.0)
    
    tori_rect=tori.get_rect() 
    tori_rect.center=(toriX,toriY)
    font=pg.font.Font(None,200)
    font1=pg.font.Font(None,100)


    while True:
        scrn_sfc.blit(bg, bg_rect)
        scrn_sfc.blit(tori,tori_rect)
        text=font.render("", True, (255,255,255))
        scrn_sfc.blit(text, [500, 400])
        text1=font1.render("[s] : start", True, (255,255,255))
        scrn_sfc.blit(text1, [500, 550])
        text2=font1.render("[c] : character", True, (255,255,255))
        scrn_sfc.blit(text2, [500, 650])
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
        pressed = pg.key.get_pressed()
        if pressed[pg.K_s]:
            mod=1
            return
        if pressed[pg.K_c]:
            mod=3
            return

def main3 ():              #GameOver画面
    global mod
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("Game Over")
    font=pg.font.Font(None,200)
    font1=pg.font.Font(None,100)

    while True:
        text=font.render("Game Over", True, (255,255,255))
        scrn_sfc.blit(text, [500, 400])
        text1=font1.render("[R] : Restart", True, (255,255,255))
        scrn_sfc.blit(text1, [500, 550])
        text1=font1.render("[E] : Exit", True, (255,255,255))
        scrn_sfc.blit(text1, [500, 650])
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pressed = pg.key.get_pressed()
        if pressed[pg.K_r]:
            mod=0
            return
        if pressed[pg.K_e]:
            pg.quit()
            sys.exit()

def main4 ():             #キャラクター選択画面
    global mod,toriping
    pg.init()
    scrn_sfc=pg.display.set_mode((1600,900))
    pg.display.set_caption("character")
    
    bg = pg.image.load("ex04/pg_bg.jpg") 
    bg_rect=bg.get_rect()  
    
    tori = pg.image.load("fig/0.png")       #こうかとん
    tori=pg.transform.rotozoom(tori,0,3.0)
    tori_rect=tori.get_rect() 
    tori_rect.center=(250,400)
    
    tori2 = pg.image.load("fig/1.png")       #こうかとん
    tori2=pg.transform.rotozoom(tori2,0,3.0)
    tori2_rect=tori.get_rect() 
    tori2_rect.center=(750,450)

    tori3 = pg.image.load("fig/2.png")       #こうかとん
    tori3=pg.transform.rotozoom(tori3,0,3.0)
    tori3_rect=tori.get_rect() 
    tori3_rect.center=(1300,400)


    font=pg.font.Font(None,150)
    font1=pg.font.Font(None,100)


    while True:
        scrn_sfc.blit(bg, bg_rect)
        scrn_sfc.blit(tori,tori_rect)
        scrn_sfc.blit(tori2,tori2_rect)
        scrn_sfc.blit(tori3,tori3_rect)
        text1=font1.render("[0]", True, (255,255,255))
        scrn_sfc.blit(text1, [200, 550])
        text2=font1.render("[1]", True, (255,255,255))
        scrn_sfc.blit(text2, [700, 550])
        text3=font1.render("[2]", True, (255,255,255))
        scrn_sfc.blit(text3, [1300, 550])
        text4=font.render("   Character Select", True, (0,0,0))
        scrn_sfc.blit(text4, [200, 100])
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                mod=0
                return
        pressed = pg.key.get_pressed()
        if pressed[pg.K_1]:
            mod=0
            toriping=1
            return
        if pressed[pg.K_0]:
            mod=0
            toriping=0
            return
        if pressed[pg.K_2]:
            mod=0
            toriping=2
            return
               

if __name__=="__main__":
    mod=0
    while True:
        if mod==0:  #スタート画面
            main2()
        if mod==1:  #ゲーム画面
            main()
        if mod==2:  #GameOver画面
            main3()
        if mod==3:  #キャラクター選択画面
            main4()