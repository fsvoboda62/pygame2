import pygame
from random import *


#class du joueur
class Monster(pygame.sprite.Sprite):

    def __init__(self,game,type_monster):
        super().__init__()
        self.health = 25
        self.attack = 10
        self.velocity = randint(1,4)
        self.marche=1
        self.image = pygame.image.load(f"assets/mummy.png")
        self.image = pygame.transform.scale(self.image,(180,180))
        self.images = []
        self.rect = self.image.get_rect()
        #self.rect.x = 1080
        self.rect.y = 490
        self.x_max = 1080
        self.x_min = -200
        self.game = game
        self.type_monster = type_monster
        if type_monster == 1:
            self.rect.x = self.x_max
        else:
            self.rect.x = self.x_min
            self.image = pygame.transform.flip(self.image, True, False)
        self.set_images()
    
    def set_images(self):
        for i in range(1,25):
            self.images.append(pygame.image.load(f"assets/mummy/mummy{i}.png"))

    def kill(self):
        print("il est mort") 
        self.game.ajoute_point()  
        self.remove()  

    def touch(self):
        print("il est touché")  
        for projectile in pygame.sprite.spritecollide(self,self.game.player.all_projectiles,0):
            self.health -= projectile.attack
            projectile.kill()
        if self.health <= 0:
            self.kill()

    def move(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.marche += 1
            if self.marche == 24:
                self.marche = 0
            self.image = self.images[self.marche]
            self.image = pygame.transform.scale(self.image,(180,180))

            if self.type_monster == 1:
                self.rect.x -= self.velocity
                if self.rect.x < self.x_min:
                    self.remove()
            else:
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect.x += self.velocity
                if self.rect.x > self.x_max:
                    self.remove()
        else:
            print("collision monster avec player")
            self.game.player.touched(self)
            self.remove()

    def remove(self):
        self.game.all_monsters.remove(self)
        