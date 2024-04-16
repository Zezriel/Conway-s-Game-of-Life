import pygame
from pygame.locals import *





test_liste = [[1,0,0,0,0,1,],[0,0,0,0,0,0,],[0,0,0,0,0,0,],[0,0,0,0,0,1]]


#initialiser la fenetre
fenetre = pygame.display.set_mode((600,600))
pygame.display.set_caption('The game of life')


def change_background_color():
    fenetre.fill((50,50,250))


def draw_square(surface,x,y,taille,color = (250,250,250)):
    pygame.draw.rect(surface,(color),(x,y,taille,taille))


def square_the_list(liste,taille,surface):
    num_ligne = len(liste)
    num_colonne = len(liste[1])
    for y in range(num_ligne):
        for x in range(num_colonne):
            if liste[y][x] == 1:
                draw_square(surface,x*taille,y*taille,taille)
            else: draw_square(surface,x*taille,y*taille,taille,(250,0,0))
            #print("draw")
    










