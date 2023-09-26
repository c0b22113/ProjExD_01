import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_fimg = pg.transform.flip(bg_img, True, False)
    kk3_img = pg.image.load("ex01/fig/3.png")
    kk3_img = pg.transform.flip(kk3_img ,True, False)
    kk3_img_10 = pg.transform.rotozoom(kk3_img, 10, 1.0)
    kk3_imgs = [kk3_img, kk3_img_10]

    tmr = 0
    x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_fimg, [1600-x, 0])

        if tmr % 2 == 0:
            screen.blit(kk3_imgs[tmr % 2], [300, 200])
        elif tmr % 2 == 1:
            screen.blit(kk3_imgs[tmr % 2], [300, 200])
        pg.display.update()
        tmr += 1
        x += 1
        clock.tick(500)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
