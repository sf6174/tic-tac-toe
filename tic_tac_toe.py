import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
line_width = 15
win_line_width = 15
bg_color = (50, 50, 50)
line_color = (55, 55, 55)
board_rows = 3
board_col = 3
square_size = 200
circle_radius = 60 
circle_width = 15
cross_width = 25
space = 55
circle_color = (32, 55, 19)
cross_color = (32, 55, 19)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC_TAC_TOE')
screen.fill(bg_color)

#Create a board
board = np.zeros((board_rows, board_col))


#Define a function to draw the horizontal and vertical lines
def screen_lines():
    #First horizontal line
    pygame.draw.line( screen, line_color, (0, 200), (600, 200), line_width)
    #Second horizontal line
    pygame.draw.line( screen, line_color, (0, 400), (600, 400), line_width)
    
    #First vertical line
    pygame.draw.line( screen, line_color, (200, 0), (200, 600), line_width)
    #Second vertical line
    pygame.draw.line( screen, line_color, (400, 0), (400, 600), line_width)
    
screen_lines()

def circle_cross():
  for row in range(board_rows):
    for col in range(board_col):
      if board[row][col] == 1:
        pygame.draw.circle( screen, circle_color, (int( col * square_size + square_size // 2), int( row * square_size + square_size // 2)), circle_radius, circle_width)
      elif board[row][col] == 2:
        pygame.draw.line( screen, cross_color, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width)
        pygame.draw.line( screen, cross_color, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)



def mark_square(row, col, player):
  board[row][col] = player

def available_square(row, col):
  if board[row][col] == 0:
    return True
  else:
    return False

def is_board_full():
  for row in range(board_rows):
    for col in range(board_col):
      if board[row][col] == 0:
        return False

  return True


def check_win(player):
  for col in range(board_col):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      draw_vertical_winning_line(col, player)
      return True

  for row in range(board_rows):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      draw_horizontal_winning_line(row, player)
      return True
  
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    draw_desc_diagonal(player)
    return True

  return False


def draw_vertical_winning_line(col, player):
  posX = col * square_size + square_size//2

  if player == 1:
    color = circle_color
  elif player == 2:
    color = cross_color

  pygame.draw.line( screen, color, (15, posX), (width - 15, posX), win_line_width)


def draw_horizontal_winning_line(row, player):
	posY = row * square_size + square_size//2

	if player == 1:
		color = circle_color
	elif player == 2:
		color = cross_color

	pygame.draw.line( screen, color, (15, posY), (width - 15, posY), win_line_width)

def draw_asc_diagonal(player):
  if player == 1:
    color = circle_color

  elif player == 2:
    color = cross_color

  pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), win_line_width)


def draw_desc_diagonal(player):
  if player == 1:
    color = circle_color

  elif player == 2:
    color = cross_color


  pygame.draw.line( screen, color, (15, 15), (width - 15, height - 15), win_line_width)


def restart():
  screen.fill( bg_color)
  screen_lines()
  for row in range(board_rows):
    for col in range(board_col):
      board[row][col] = 0


screen_lines

#Variables
player = 1
game_over = False

player = 1

#Create main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
          

          mouseX = event.pos[0]
          mouseY = event.pos[1]

          clicked_row = int(mouseY // square_size)
          clicked_col = int(mouseX // square_size)

          if available_square( clicked_row, clicked_col):

            mark_square(clicked_row, clicked_col, player)
            if check_win(player):
              game_over = True

            player = player % 2 + 1

            circle_cross()

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            restart()
            player = 1
            game_over = False


          
    pygame.display.update()
    