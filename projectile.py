import pygame

#class du joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self,player,type_projectile):
        super().__init__()
        pygame.mixer.music.load("assets/sounds/tir.ogg")
        pygame.mixer.music.play()
        self.velocity = 12
        self.attack = 25
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image_origin = self.image
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.y = player.rect.y + 80
        self.player = player
        self.type_projectile = type_projectile
        if type_projectile == 1:
            self.rect.x = player.rect.x + 120
        else:
            self.rect.x = player.rect.x 

    def kill(self):
        self.remove()
    
    def remove(self):
        self.player.all_projectiles.remove(self)

    def rotate(self):
        if self.type_projectile == 1:
            self.angle -= 12
        else:
            self.angle += 12
        self.image = pygame.transform.rotate(self.image_origin, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.angle >= 360:
            self.angle = 0
    
    def move(self):
        monster_touched=(self.player.game.check_collision(self,self.player.game.all_monsters))
        if not monster_touched:
            self.rotate()
            if self.type_projectile == 1:
                self.rect.x += self.velocity
                if self.rect.x > 1080:
                    self.remove()
            else:
                self.rect.x -= self.velocity
                if self.rect.x < 0:
                    self.remove()
        else:
            print("collision projectile / monstre")
            monster_touched[0].touch()
            self.remove()
            
