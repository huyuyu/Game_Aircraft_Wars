import pygame
from bullet import *
import random

class Plane(object):
    def __init__(self, screen, plane_name):
        self.plane_name = plane_name
        # 设置要显示内容的窗口
        self.screen = screen
        # 根据图片的名称生成飞机图片
        self.image = pygame.image.load(self.image_name).convert()
        # 用来储存英雄飞机发射的所有子弹，将子弹显示在飞机上方
        self.bullet_list = []

    def display(self):
        # 更新飞机的位置
        self.screen.blit(self.image, (self.x, self.y))
       
        # 用来存放需要删除的对象
        need_del_list = []
        # 保存需要删除的对象
        for item in self.bullet_list:
            if item.judge():
                need_del_list.append(item)
        # 删除需要删除的对象
        for del_item in need_del_list:
            need_del_list.remove(del_item)

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def launch_bullet(self):
        new_bullet = PublicBullet(self.x, self.y, self.screen, self.plane_name)
        self.bullet_list.append(new_bullet)

class HeroPlane(Plane):

    def __init__(self, screen, plane_name):
        self.x = 230
        self.y = 600
        self.image_name = './hero.png'
        super().__init__(screen, "hero")

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

class EnemyPlane(Plane):

    def __init__(self, screen, plane_name):
        self.x = 0
        self.y = 0
        self.image_name = './hero.png'
        super().__init__(screen, "enemy")
        # 用来记录敌人飞机的初始移动方向
        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            self.x += 2
        elif self.direction == 'left':
            self.x -= 2
        if self.x > 480-50:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def launch_bullet(self):
        number = random.randint(1, 100)
        if number == 88:
            super().launch_bullet()