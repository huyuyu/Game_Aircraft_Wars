import pygame, time
from pygame.locals import *
from plane import *

def start():
    # 创建一个480*890的窗口
    screen = pygame.display.set_mode((480, 890), 0, 32)
    image_file_path = './background.jpg'
    background = pygame.image.load(image_file_path).convert()
    hero_pland = HeroPlane(screen, "hero")
    enemy_plane = EnemyPlane(screen, "enemy")

    # 将图片设置在坐标（0，0）的位置，并保证背景图片一直在屏幕上
    while True:  
        screen.blit(background, (0, 0))
        hero_pland.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()
        # time.sleep(0.1)
        pygame.display.update()

        # 添加检测到的鼠标和键事件的代码
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    hero_pland.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    hero_pland.move_right()
                elif event.key == K_SPACE:
                    print("space")  
                    hero_pland.launch_bullet()                  

if __name__ == "__main__":
    start()