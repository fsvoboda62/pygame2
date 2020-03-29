import pygame
from projectile import Projectile

#class du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.health_bonus = 30
        self.velocity = 10
        self.max_projectile = 4
        self.image = self.init_image(False)
        self.rect = self.image.get_rect()
        self.images = []
        self.set_images()
        self.rect.x = 300
        self.rect.y = 500
        self.x_max = 860
        self.x_min = 5
        self.all_projectiles = pygame.sprite.Group()
        self.game=game
        

    def set_images(self):
        for i in range(1,25):
            self.images.append(pygame.image.load(f"assets/player/player{i}.png"))

    def init_image(self,flip : "retourner l'image - True image retournée sinon False") -> pygame.image: # une image de pygame
        image = pygame.image.load("assets/player/player1.png") 
        if flip:
            image = pygame.transform.flip(image, True, False)
        return image


    def touched(self,objet : "Objet monster/meteorite avec un paramétre ATTACK"):
        print("je suis touché")
        self.health -= objet.attack
        if self.health <= 0:
            print("Je suis mort... GAME OVER")
            self.game.running = False

    def ajoute_vie(self):
        self.health += self.health_bonus
        if self.health >= self.max_health:
            self.health = self.max_health

    def lauch_projectile(self,type : "1=Se déplace vers la gauche sinon 2"):
        #ajoute le projectile    
        if len(self.all_projectiles)<self.max_projectile:
            # fait le mouvement de la main
            for i in range(0,24):
                self.image = self.images[i]
                if type == 2:
                    self.image = pygame.transform.flip(self.image, True, False)
                # redessine l'ecran
                self.game.screen.blit(self.image, self.rect)
                pygame.display.flip()
            self.image = self.init_image(False)
            if type == 2:
                self.image = pygame.transform.flip(self.image, True, False)
            self.all_projectiles.add(Projectile(self,type))

    def move_right(self):
        self.image = self.init_image(False)
        if not self.game.check_collision(self,self.game.all_monsters):
            if self.rect.x<=self.x_max:
                self.rect.x += self.velocity

    def move_left(self):
        self.image = self.init_image(True)
#        if not self.game.check_collision(self,self.game.all_monsters):
        if self.rect.x>=self.x_min:
            self.rect.x -= self.velocity
