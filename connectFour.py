# importing some libraries
import time
import math
import random
import pyfiglet
import sys
import threading

# adding some aesthetics for coolness
font = pyfiglet.Figlet(font='slant')
font2 = pyfiglet.Figlet(font='standard')
welcome_ascii = font2.renderText('Welcome To The Game Of ')
loading_ascii = font.renderText('Loading')
twist_ascii = font.renderText('...with a twist!')

ascii_art = font.renderText('Connect Four!')



"""
Name: Emily Dogbatse & Davis Carson
Assignment: CONNECT 4 GAME
Class: CMS430

Can you beat the COMPUTER_ALPHA_BETA....? No...we can't. But its worth a shot..
I guess...

"""

# STEP ONE (DONE)
# write a simple version of the game for one player (DONE)

# STEP TWO (DONE)
# write a simple version of the game for two players (DONE)

# STEP THREE (START HERE)
# Replace the second player with the minimax algorithm

# STEP FOUR (LAST STEP)
# ADD alpha beta pruning


# Initialize the board,which should be a 7 col x 6 board
ROW = 6
COL = 7
# board using list comprehension
board = [[0 for j in range(COL)] for i in range(ROW)]

# function to print out the loading screen
class LoadingAnimation(threading.Thread):
  def __init__(self):
      super().__init__()
      self.stop_event = threading.Event()

  def run(self):
      animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
      while not self.stop_event.is_set():
          for frame in animation:
              print(f"\rLoading {frame}", end="")
              time.sleep(0.1)

def print_slow(text, delay = 0.5):
  for char in text:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(delay)
  print()


# players
PLAYER = 1
COMPUTER_ALPHA_BETA = 2

# small add on randomize who starts the game
if random.randint(0, 1) == 0:
    current_player = PLAYER
else:
    current_player = COMPUTER_ALPHA_BETA

# function to print out the game board

def print_board():
  print("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
  for row in board:
    print("║", end="")
    for col in row:
      if col == 0:
        print("   ║", end="")
      elif col == PLAYER:
        print(" X ║", end="")
      else:
        print(" O ║", end="")
    print("\n╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
print("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╝")
print("  0   1   2   3   4   5   6")


# function to define a winner (this function checks 4 in a row horizontally, diagonally, and then vertically)
def check_winner(player):
    # checks the horizontal
    for row in range(ROW):
        for col in range(COL - 3):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    # checks the vertical
    for row in range(ROW - 3):
        for col in range(COL):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # checks for the diagonal (positive)
    for row in range(ROW - 3):
        for col in range(COL - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # checks for the diagonal (negative)
    for row in range(ROW - 3):
        for col in range(3, COL):
            if board[row][col] == player and board[row + 1][col - 1] == player and board[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                return True

    return False

# evaluates for a win on the board
def score():
    if check_winner(COMPUTER_ALPHA_BETA):
        return 1
    elif check_winner(PLAYER):
        return -1
    else:
        return 0

# implementing the last step for the minimax algorithm with alpha beta pruning
def minimax(depth, alpha, beta, player):
    best_value = score()
    if best_value == 1:
        return best_value
    if best_value == -1:
        return best_value
    if depth == 0:
        return 0

    if player == COMPUTER_ALPHA_BETA:
        best_score = -float("inf")
        for col in range(COL):
            row = next_open_row(col)
            if row != -1:
                board[row][col] = COMPUTER_ALPHA_BETA
                current_score = minimax(depth - 1, alpha, beta, PLAYER)
                board[row][col] = 0
                best_score = max(best_score, current_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float("inf")
        for col in range(COL):
            row = next_open_row(col)
            if row != -1:
                board[row][col] = PLAYER
                current_score = minimax(depth - 1, alpha, beta, COMPUTER_ALPHA_BETA)
                board[row][col] = 0
                best_score = min(best_score, current_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# finding the next open row
def next_open_row(col):
    for row in range(ROW - 1, -1, -1):
        if board[row][col] == 0:
            return row
    return -1

# function to define the human moves
def player_move():
    valid_move = False
    while not valid_move:
        col = int(input("Enter a column (0-6): "))
        if col < 0 or col > 6:
            print("Invalid column. Try again.")
        else:
            row = next_open_row(col)
            if row == -1:
                print("Nope! Too full! Try again.")
            else:
                board[row][col] = PLAYER
                valid_move = True

# function to define the computer's move and implement the alpha beta pruning
def comp_move():
    best_score = -float("inf")
    best_col = None
    for col in range(COL):
        row = next_open_row(col)
        if row != -1:
            board[row][col] = COMPUTER_ALPHA_BETA
            score = minimax(5, -float("inf"), float("inf"), PLAYER)
            board[row][col] = 0
            if score > best_score:
                best_score = score
                best_col = col
    row = next_open_row(best_col)
    board[row][best_col] = COMPUTER_ALPHA_BETA

# welcome screen 
print(welcome_ascii)
print("######################################################")
print(ascii_art)
print(twist_ascii)

print("""
╔═══════════════════════════════════════════╗
║                                           ║
║   1. Play                                 ║
║   2. Exit                                 ║
║   3. Options                              ║
║                                           ║
╚═══════════════════════════════════════════╝
""")

print(loading_ascii)
print()

loading_animation = LoadingAnimation()
loading_animation.start()
time.sleep(random.uniform(3, 6))  # Random delay between 3-6 seconds

loading_animation.stop_event.set()  # Stop the loading animation
loading_animation.join()



print("\n.... Did you know that pruning is actually a gardening term?")
time.sleep(3)
print_slow("Printing the game board...", delay=0.05)
time.sleep(2)

print_slow("Fixing the pieces together...", delay=0.05)
time.sleep(2)


print_slow("\nLoading complete!\n", delay=0.05)


print("Player 1: You are X's.")
time.sleep(1)

print("Player 2: You are O's.")
time.sleep(2)

# run the game here
while True:

    print_board()
    if current_player == PLAYER:
        player_move()
        if check_winner(PLAYER):
            print("...this should NOT have happened...")
            break
        current_player = COMPUTER_ALPHA_BETA
    else:
        comp_move()
        if check_winner(COMPUTER_ALPHA_BETA):
            print("Yes....the computer wins once again. 2000 Level IQ that humans will never achieve! >:)")
            break
        current_player = PLAYER
    if all(all(row) for row in board):
        print("Its....a tie?....This also should NOT have happened...go back and try again!")
        break
