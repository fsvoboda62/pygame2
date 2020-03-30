import pygame
from player import Player
from monster import Monster
from meteorite import Meteorite

#class du Jeu
class Game():

    def __init__(self,screen):
        #ajout d'un joueur
        self.screen = screen
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.all_meteorites = pygame.sprite.Group()
        self.pressed={}
        self.running = True
        self.game_over = False
        self.point = 0
        self.sound_Game_Over = pygame.mixer.Sound("assets/sounds/game_over.ogg")
        self.play_song = True
        self.niveau = 1
        self.mode = 1
    
    def __del__(self):
        print("dans le destructeur")

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def add_attack(self,type :"1=Se déplace vers la gauche sinon 2"):
        if self.mode == 1: #attaque de monstres
            print("on ajoute un monstre")
            self.all_monsters.add(Monster(self,type))
        else: #attaque de météorites
            print("on ajoute une météorite")
            self.all_meteorites.add(Meteorite(self))

    def add_monster(self, type):
        self.all_monsters.add(Monster(self,type))

    def add_meteorite(self):
        self.all_meteorites.add(Meteorite(self))

    def ajoute_point(self):
        self.point += 1
        print(self.point%10)
        if self.point%10 == 0:
            self.mode += 1
            self.player.ajoute_vie()
            if self.mode == 3:
                self.mode = 1
                self.niveau += 1 
