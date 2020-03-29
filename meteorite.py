import pygame
from random import *


#class du joueur
class Meteorite(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        pygame.mixer.music.load("assets/sounds/meteorite.ogg")
        pygame.mixer.music.play()
        self.attack = 10
        self.velocity = randint(5,10)
        self.image = pygame.image.load(f"assets/comet.png")
        #self.image = pygame.transform.scale(self.image,(180,180))
        self.rect = self.image.get_rect()
        self.rect.x = randint(10,950)
        self.rect.y = 0
        self.y_max = 700
        
    # def kill(self):
    #     print("il est mort") 
    #     self.game.ajoute_point()  
    #     self.remove()  

    # def touch(self):
    #     print("il est touché")  
    #     for projectile in pygame.sprite.spritecollide(self,self.game.player.all_projectiles,0):
    #         self.health -= projectile.attack
    #         projectile.kill()

    #     if self.health <= 0:
    #         self.kill()

    def move(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.y += self.velocity
            if self.rect.y >= self.y_max:
                self.game.ajoute_point() 
                self.remove()
        else:
            self.game.player.touched(self)
            self.remove()
            print("collision meteorite / player")

        monster_touched = self.game.check_collision(self,self.game.all_monsters)
        if monster_touched:
            monster_touched[0].remove()
            

    
    def remove(self):
        self.game.all_meteorites.remove(self)
        