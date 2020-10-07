import pygame
import os
import DrawingFunctions
from board.Board import Board
# Constants


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 960
GAME_WIDTH = 960
GAME_HEIGHT = 960
DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

WINDOW_STARTING_X_POS = 480
WINDOW_STARTING_Y_POS = 50

BLOCK_SIZE = 120
PIECE_PADDING = 20
FPS = 144

BROWN = (58, 38, 19)
WHITE = (200, 200, 200)


def main():
    # Drawing the board
    DrawingFunctions.draw_board(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, WHITE, BROWN)

    # Drawing the pieces on the board
    DrawingFunctions.draw_pieces(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, PIECE_PADDING)

    # Initializing our game board
    board = Board()
    board.fill()

    # Setting up the game loop
    running = True
    white_turn = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


def test():
    b = Board()
    b.fill()


# Initializing the game
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_STARTING_X_POS},{WINDOW_STARTING_Y_POS}'  # Setting the initial starting position of the window in the middle of the screen
pygame.init()

# Creating the game and setting global variables up
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()     # FPS clock


# Starting the game
main()
test()


