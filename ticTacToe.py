#import needed libraries 
import sys
import numpy
import pygame

#create game window
pygame.init()

#color variable
WHITE = (225, 255, 255)
GRAY = (180, 180, 180)
RED = (255, 0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

#Proportions
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

#Define window display
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Resolution
pygame.display.set_caption('Tic Tac Toe AI') #Window Title
screen.fill(BLACK) #Window background color
board = numpy.zeros((BOARD_ROWS, BOARD_COLS))

#Define Methods
def draw_lines(color=WHITE):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:  # Player 1 (O)
                pygame.draw.circle(screen, WHITE, 
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:  # Player 2 (X)
                pygame.draw.line(screen, WHITE, 
                                 (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), CROSS_WIDTH)
                pygame.draw.line(screen, WHITE, 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), 
                                 (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), CROSS_WIDTH)

# Function to mark a square on the board
def mark_square(row, col, player):
    board[row][col] = player

# Function to check if a square is available
def available_square(row, col):
    return board[row][col] == 0

# Function to check if the board is full
def is_board_full():
    return not (0 in board)

# Function to check if a player has won
def check_win(player, check_board=board):
    # Check vertical win condition
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
    # Check horizontal win condition
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
    # Check diagonal win conditions
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:  # Left-top to right-bottom
        return True
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:  # Right-top to left-bottom
        return True
    return False

# Display winner message
def display_winner(player):
    font = pygame.font.Font(None, 40)  # Set font size
    text = font.render(f"Player {player} Wins!", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center text
    screen.blit(text, text_rect)  # Render text on screen
    pygame.display.update()  # Update display

# MinMax AI Function(s)
def minmax(minimax_board, depth, is_maximizing):
    if check_win(2, minmax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minmax_board):
        return 0

# Game variables
player = 1  # Player 1 starts
game_over = False  # Game state

# Initial rendering
draw_lines()
pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                draw_figures()
                pygame.display.update()  # Update display immediately

                if check_win(player):  # If player wins, show message
                    game_over = True
                    display_winner(player)  # Show winner message
                    continue  # Skip player switch

                # If board is full and no player win, display draw message
                if is_board_full():  
                    game_over = True
                    font = pygame.font.Font(None, 40)
                    text = font.render("Draw!", True, WHITE)
                    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    continue  # End game loop

                player = 3 - player  # Switch player
