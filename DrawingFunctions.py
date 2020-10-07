import pygame


# Draws a chess board to the screen
def draw_board(screen, screen_width, screen_height, block_size, color_1, color_2):
    for x in range(screen_width // block_size):
        for y in range(screen_height // block_size):
            rect = pygame.Rect(y * block_size, x * block_size, block_size, block_size)
            __draw_right_color(screen, x, y, color_1, color_2, rect)


# Draws an image to the screen
def draw_image(screen, path, coordinates):
    img = pygame.image.load(path)
    screen.blit(img, coordinates)


# Removes a piece from the board
def remove_piece(screen, block_size, x, y, color_1, color_2):
    rect = pygame.Rect(y * block_size, x * block_size, block_size, block_size)
    __draw_right_color(screen, x, y, color_1, color_2, rect)


# Chooses and draws the right colored rectangle according to the coordinates on the board
def __draw_right_color(screen, x, y, color_1, color_2, rect):
    if x % 2 == 0:
        if y % 2 == 0:
            pygame.draw.rect(screen, color_1, rect)
        else:
            pygame.draw.rect(screen, color_2, rect)
    else:
        if y % 2 != 0:
            pygame.draw.rect(screen, color_1, rect)
        else:
            pygame.draw.rect(screen, color_2, rect)


# Draws all the pieces in the starting position
def draw_pieces(screen, screen_width, screen_height, block_size, padding):

    # Black rooks
    draw_image(screen, r'media\rook_b.png', (padding, padding))
    draw_image(screen, r'media\rook_b.png', (screen_width - block_size + padding, padding))

    # White rooks
    draw_image(screen, r'media\rook.png', (padding, screen_height - block_size + padding))
    draw_image(screen, r'media\rook.png', (screen_width - block_size + padding, screen_height - block_size + padding))

    # Black knights
    draw_image(screen, r'media\knight_b.png', (block_size + padding, padding))
    draw_image(screen, r'media\knight_b.png', (screen_width - block_size * 2 + padding, padding))

    # White knights
    draw_image(screen, r'media\knight.png', (block_size + padding, screen_height - block_size + padding))
    draw_image(screen, r'media\knight.png', (screen_width - block_size * 2 + padding, screen_height - block_size + padding))

    # Black bishops
    draw_image(screen, r'media\bishop_b.png', (block_size * 2 + padding, padding))
    draw_image(screen, r'media\bishop_b.png', (screen_width - block_size * 3 + padding, padding))

    # White bishops
    draw_image(screen, r'media\bishop.png', (block_size * 2 + padding, screen_height - block_size + padding))
    draw_image(screen, r'media\bishop.png', (screen_width - block_size * 3 + padding, screen_height - block_size + padding))

    # Queens
    draw_image(screen, r'media\queen_b.png', (block_size * 3 + padding, padding))
    draw_image(screen, r'media\queen.png', (block_size * 3 + padding, screen_height - block_size + padding))

    # Kings
    draw_image(screen, r'media\king_b.png', (block_size * 4 + padding, padding))
    draw_image(screen, r'media\king.png', (block_size * 4 + padding, screen_height - block_size + padding))

    # Pawns
    for i in range(screen_width // block_size):
        draw_image(screen, r'media\pawn_b.png', (block_size * i + padding, block_size + padding))
        draw_image(screen, r'media\pawn.png', (block_size * i + padding, screen_height - block_size * 2 + padding))

