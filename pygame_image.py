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
    count = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if x >= 1600:
            count = 1 if count == 0 else 0
            x = 0

        if count == 0:
            screen.blit(bg_img, [-x, 0])
            screen.blit(bg_fimg, [1600 - x, 0])
        else:
            screen.blit(bg_fimg, [-x, 0])
            screen.blit(bg_img, [1600 - x, 0])

        index = (tmr // 75) % 2
        screen.blit(kk3_imgs[index], [300, 200])

        pg.display.update()
        tmr += 1
        x += 1
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
