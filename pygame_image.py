import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk3_img = pg.image.load("ex01/fig/3.png")
    kk3_img = pg.transform.flip(kk3_img ,True, False)
    kk2_img = pg.image.load("ex01/fig/2.png")
    kk2_img_10 = pg.transform.rotate(kk2_img, 10)
    kk2_list = [kk2_img, kk2_img_10]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk3_img, [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
