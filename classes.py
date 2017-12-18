import pygame
from pygame.locals import *
from constantes import *

class Niveau:
    def __init__(self, choix):
        self.fichier = choix+".niveau"
        self.structure = 0

    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                    structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau


    def afficher(self, fenetre):
        mur = pygame.image.load(image_mur).convert_alpha()
        depart = pygame.image.load(image_depart).convert_alpha()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()


class Perso:
        def __init__(self, droite, gauche, haut, bas, niveau):
                self.droite = pygame.image.load(droite).convert_alpha()
                self.gauche = pygame.image.load(gauche).convert_alpha()
                self.haut = pygame.image.load(haut).convert_alpha()
                self.bas = pygame.image.load(bas).convert_alpha()
                self.case_x = 0
                self.case_y = 0
                self.x = 0
                self.y = 0
                self.direction = self.droite
                self.niveau = niveau

        def deplacer(self, direction):
                if direction == 'droite':
                	if self.case_x < (nombre_sprite_cote - 1):
                		if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                			self.case_x += 1
                			self.x = self.case_x * taille_sprite
                	self.direction = self.droite

                if direction == 'gauche':
                	if self.case_x > 0:
                		if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                			self.case_x -= 1
                			self.x = self.case_x * taille_sprite
                	self.direction = self.gauche

                if direction == 'haut':
                	if self.case_y > 0:
                		if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                			self.case_y -= 1
                			self.y = self.case_y * taille_sprite
                	self.direction = self.haut

                if direction == 'bas':
                	if self.case_y < (nombre_sprite_cote - 1):
                		if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                			self.case_y += 1
                			self.y = self.case_y * taille_sprite
                	self.direction = self.bas
