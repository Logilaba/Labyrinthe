import pygame
from pygame.locals import *
import classes
import constantes
import fonctions

def boucle_accueil(continuer_accueil):
    while continuer_accueil:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            choix = ""
            if (event.type == QUIT
                or event.type == KEYDOWN
                and event.key == K_ESCAPE):
                # continuer_accueil = 0
                # continuer_jeu = 0
                # continuer = 0
                choix = "quit"
            elif event.type == KEYDOWN:
                if event.key == K_F1:
                    # continuer_accueil = 0
                    choix = "n1"
                elif event.key == K_F2:
                    # continuer_accueil = 0
                    choix = "n2"

            return choix
