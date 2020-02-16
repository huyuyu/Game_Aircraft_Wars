import pygame

class PublicBullet(object):
    
    def __init__(self, x, y, screen, plane_name):
        self.screen = screen
        self.plane_name = plane_name

        if self.plane_name == 'hero':
            self.x = x + 40
            self.y = y - 20
            self.image_name = './bullet.jpg'
        elif self.plane_name == 'enemy':
            self.x = x + 30
            self.y = y + 30
            self.image_name = './enemy_bullet.png'
        self.image = pygame.image.load(self.image_name).convert()

    def move(self):
        if self.plane_name == 'hero':
            self.y -= 2
        elif self.plane_name == 'enemy':
            self.y += 2

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def judge(self):
        if self.y > 890 or self.y < 0 :
            return True
        else:
            return False






# class Bullet(object):
#     def __init__(self, x, y, screen):
#         self.x = x + 40
#         self.y = y - 20
#         self.screen = screen
#         self.image = pygame.image.load('./bullet.jpg').convert()
    
#     def display(self):
#         self.screen.blit(self.image, (self.x, self.y))

#     def move(self):
#         self.y -= 2

#     def judge(self):
#         if self.y < 0:
#             return True
#         else:
#             return False

# class EnemyBullet(object):
#     def __init__(self, x, y, screen):
#         self.x = x + 30
#         self.y = y + 30
#         self.screen = screen
#         self.image = pygame.image.load('./bullet.jpg').convert()

#     def move(self):
#         self.y += 2
    
#     def display(self):
#         self.screen.blit(self.image, (self.x, self.y))

#     def judge(self):
#         if self.y > 890 :
#             return True
#         else:
#             return False


