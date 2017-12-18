import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
pygame.key.set_repeat(400, 30)
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:	#Si clic gauche
				#On change les coordonnées du perso
				perso_x = event.pos[0]
				perso_y = event.pos[1]

	#Re-collage
	fenetre.blit(fond, (0,0))
	fenetre.blit(perso, (perso_x, perso_y))
	#Rafraichissement
	pygame.display.flip()
