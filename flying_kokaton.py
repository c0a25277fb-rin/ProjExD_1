import os
import sys
import math
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    # こうかとん
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    kk_rct = kk_img.get_rect()
    kk_rct.center = (400, 300)

    # 文字
    fonto = pg.font.Font(None, 30)
    txt = fonto.render(
        "HELLO !! TOKYO UNIVERSITY OF TECHNOLOGY",
        True,
        (0, 0, 0)
    )

    txt_rct = txt.get_rect()
    txt_rct.center = (400, 100)

    tmr = 0

    # 背景の移動速度
    bg_speed = 20

    # こうかとんの移動速度
    bird_speed = 8

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # キー入力
        key_lst = pg.key.get_pressed()

        # 背景を高速で移動させる
        x = (tmr * bg_speed) % 3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # こうかとんを上下に移動させる
        if key_lst[pg.K_UP]:
            # kk_rct.y -= bird_speed
            kk_rct.move_ip((0,-1))

        if key_lst[pg.K_DOWN]:
            # kk_rct.y += bird_speed
            kk_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((+1,0))


        # 画面から出ないようにする
        if kk_rct.top < 0:
            kk_rct.top = 0

        if kk_rct.bottom > 600:
            kk_rct.bottom = 600

        # 文字を表示する
        screen.blit(txt, txt_rct)

        # こうかとんを表示する
        screen.blit(kk_img, kk_rct)

        pg.display.update()

        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
