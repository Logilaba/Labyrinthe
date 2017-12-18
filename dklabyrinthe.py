import pygame
from pygame.locals import *
from classes import *
import constantes
import fonctions
"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode(
    (constantes.cote_fenetre, constantes.cote_fenetre), RESIZABLE)
#Icone
icone = pygame.image.load(constantes.image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(constantes.titre_fenetre)

continuer = 1
while continuer:
    accueil = pygame.image.load(constantes.image_accueil).convert()
    fenetre.blit(accueil, (0,0))
    pygame.display.flip()
    continuer_jeu = 1
    continuer_acceuil = 1

    choix = fonctions.boucle_accueil(continuer_acceuil)
    if choix !="":
        continuer = 0

print("choix vaut ", choix)

fond = pygame.image.load(constantes.image_fond).convert()
niveau = Niveau(choix)
niveau.generer()
niveau.afficher(fenetre)

dk = Perso("images/dk_droite.png", "images/dk_gauche.png",
            "images/dk_haut.png", "images/dk_bas.png", niveau)

while continuer_jeu:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer_jeu = 0
            continuer = 0
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                continuer_jeu = 0
            elif event.key == K_RIGHT:
                dk.deplacer('droite')
            elif event.key == K_LEFT:
                dk.deplacer('gauche')
            elif event.key == K_UP:
                dk.deplacer('haut')
            elif event.key == K_DOWN:
                dk.deplacer('bas')

    fenetre.blit(fond, (0,0))
    niveau.afficher(fenetre)
    fenetre.blit(dk.direction, (dk.x, dk.y))
    pygame.display.flip()

    if niveau.structure[dk.case_y][dk.case_x] == 'a':
        continuer_jeu = 0
        print("victoire!")
