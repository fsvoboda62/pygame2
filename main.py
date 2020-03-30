import pygame

from random import *
from game import Game

color_score = (132,180,255)
windows_resolution = (1080,720)

pygame.init()
clock = pygame.time.Clock()

#Fenetre du jeuxr
pygame.display.set_caption("BobodaGame")
screen = pygame.display.set_mode(windows_resolution)

#fond du jeux
background = pygame.image.load('assets/bg.jpg')

#Font de score et vie
arial_font = pygame.font.SysFont("arial",36)

#charger le joueur
game=Game(screen)

#temps que running est true
#running = Truer
while game.running:
    clock.tick(30)
    #fermeture de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]=True

            if event.key == pygame.K_e:
                game.player.lauch_projectile(2)
            if event.key == pygame.K_r:
                game.player.lauch_projectile(1)
            if event.key == pygame.K_UP:
                game.niveau += 1
            if event.key == pygame.K_DOWN:
                game.add_meteorite()

            if event.key == pygame.K_ESCAPE:
                game.running = False

        elif event.type == pygame.KEYUP:
            game.pressed[event.key]=False


    if randint(1,100)>(99-(game.niveau)):
        #game.add_monster(randint(1,2))
        #game.add_meteorite()
        game.add_attack(randint(1,2))
        #game.add_attack(1)


    #appliquer l'image de fond
    screen.blit(background, (0,-200))

    #score
    text_score = arial_font.render(f"SCORE : {game.point}", True, color_score)
    text_vie = arial_font.render(f"VIE : {game.player.health}", True, color_score)
    text_niveau = arial_font.render(f"NIVEAU : {game.niveau}", True, color_score)
    
    screen.blit(text_score, (10,10))
    screen.blit(text_vie, (200,10))
    screen.blit(text_niveau, (900,10))
    
    #detecte les touches
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    #appliquer le player
    screen.blit(game.player.image,game.player.rect)

    #bouge les projectiles vers la droite
    for projectile in game.player.all_projectiles:
        projectile.move()

    for monster in game.all_monsters:
        monster.move()
    
    for meteorite in game.all_meteorites:
        meteorite.move()

    #affiche le groupe de projectiles et de monstres
    game.player.all_projectiles.draw(screen)

    game.all_monsters.draw(screen)
    game.all_meteorites.draw(screen)
   
    #mise a jour de l'ecran
    pygame.display.flip()

game.sound_Game_Over.play()
pygame.quit()
print("FIN DU JEU... GAME OVER")



        

