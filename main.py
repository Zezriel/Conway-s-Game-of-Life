import random
import time
import os
import pygame_render
import pygame
pygame.init()


fenetre = pygame.display.set_mode((600,600))
pygame.display.set_caption('The game of life')
    # Boucle principale






def dead_state(width, height):
    grid = []

    for _ in range(height):
        row = [0]* width
        grid.append(row)
    return grid

def random_state(width,height):
    state = dead_state(width,height)

    for index in range(height):
        for x in range(width):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 1
            else: cell_state = 0

            state[index][x] = cell_state
    return state


def render(board_state):
    num_row = len(board_state)
    num_col = len(board_state[1])
    for x in range(num_row):
        for y in range(num_col):
            if board_state[x][y] == 1:
                    if y == num_col-1:
                        print("\u25A0  ")
                    else:print("\u25A0  ",end="")

            else:
                    if y == num_col-1:
                        print("  ")
                    else:print("   ",end="")



def next_board_state(initial_board_state):
    num_row = len(initial_board_state)
    num_col = len(initial_board_state[1])
    new_state = dead_state(num_col, num_row)
    for ligne in range(num_row): #cycle les lignes
         for colonne in range(num_col): #cycle les colonnes
                
                active_cell = initial_board_state[ligne][colonne] #recupere la valeur de la cellule actuelement observer
                live_cell = 0


                #indice des cellules voisines
                for i in range(-1, 2):
                     for j in range(-1, 2):
                            #ignorer la cellule actuelle
                            if i == 0 and j == 0:
                                 continue
                            
                            # Calculer les indices des cellules voisines
                            neighbor_row = ligne + i
                            neighbor_col = colonne + j

                            # Vérifier si la cellule voisine est dans les limites du tableau
                            if 0 <= neighbor_row < num_row and 0 <= neighbor_col < num_col:
                                 # Incrémenter le compteur de cellules vivantes si la cellule voisine est vivante
                                 live_cell += initial_board_state[neighbor_row][neighbor_col]



                #application des regle du jeux
                if active_cell == 1:# si la cellule est vivante
                    if live_cell < 2 or live_cell > 3:
                         new_state[ligne][colonne] = 0
                    else:
                         new_state[ligne][colonne] = 1
                else : #si la cellule est morte
                    if live_cell == 3: # si la cellule la 3 voisin
                         new_state[ligne][colonne] = 1

                
                
                #print(f"live cell{live_cell} index_row {ligne} index_col{colonne}")
    return new_state
                
                


def load_board_state(file):
    state = []
    with open(file, "r") as open_file:
        for line in open_file:
            row = [int(char) for char in line.strip()]
            state.append(row)
    return state



def user_choice():
     pass
                     


initial_board_state = load_board_state("GosperGliderGun.txt")



board = next_board_state(initial_board_state)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame_render.square_the_list(board,10,fenetre)
    pygame.display.flip()
    x = 0
    while x < 1000:
        board = next_board_state(board)
        pygame_render.square_the_list(board,10,fenetre)
        pygame.display.flip()
        time.sleep(0.1)
        os.system("cls")
        x +=1
pygame.quit()

#x = 0
#while x < 1000:
#     board = next_board_state(board)
#     render(board)
#     time.sleep(0.1)
#     os.system("cls")
#     x +=1