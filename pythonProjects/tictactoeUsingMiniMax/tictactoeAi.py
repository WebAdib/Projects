import copy
import random
import subprocess
import sys
import time #allows access to system-specific parameters and functions through the sys module.
import pygame #offers functionality to handle various aspects of game development, including graphics, sound, input devices like keyboards and mice, and more
import numpy as np #provides support for multi-dimensional arrays and matrices along with a collection of mathematical functions to operate on these arrays.
from constants import *


#pygame
pygame.init()# Initialize Pygame modules
screen = pygame.display.set_mode((width, height))# Create a display surface (window) with specified width and height
pygame.display.set_caption('Tic-Tac-Toe-Ai') # Set the caption (title) of the game window
screen.fill(bg_colour)# Fill the screen with the specified background color

if len(sys.argv) > 1:
    received_values = sys.argv[1].split()  # Split the received string back into separate values
    if len(received_values) >= 2:  # Check if at least two values were received
        gmd = int(received_values[0])  # Assign the first value
        pl = int(received_values[1])   # Assign the second value
        #print(f"Value 1: {gmd}, Value 2: {pl}")
    else:
        gmd = 3  # Default value if no mode argument is passed
        pl = 1
else:
    gmd = 3  # Default value if no mode argument is passed
    pl = 1

class Board:
    def __init__(self):
        self.squares = np.zeros((rows,cols))# Create an empty board using NumPy's zeros function with dimensions rows x cols
        self.empty_sqrs = self.squares # [squares]
        self.marked_sqrs = 0

    def final_state(self, show=False):
        '''
            @return 0 if there is no win yet
            @return 1 if player 1 wins
            @return 2 if player 2 wins
        '''

        # Check for vertical wins
        for col in range(cols):
            # Check if all elements in a column are equal and not equal to 0 (indicating a win)
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                # If 'show' is True, draw a line to visualize the winning pattern
                if show:
                    # Set 'color' based on the value in the squares array
                    #  Use 'circ_color' if the value at squares[0][col] is 2, otherwise use 'cross_color'
                    color = circ_color if self.squares[0][col] == 2 else cross_color
                    iPos = (col * sqsize + sqsize // 2, 20)# Calculate the starting position of the line on the board
                    fPos = (col * sqsize + sqsize // 2, height - 20)# Calculate the ending position of the line on the board
                    pygame.draw.line(screen, color, iPos, fPos, line_width)
                # Return the winning player number    
                return self.squares[0][col]

        # Check for horizontal wins
        for row in range(rows):
            # Check if all elements in a row are equal and not equal to 0 (indicating a win)
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                # If 'show' is True, draw a line to visualize the winning pattern
                if show:
                    color = circ_color if self.squares[row][0] == 2 else cross_color
                    iPos = (20, row * sqsize + sqsize // 2)
                    fPos = (width - 20, row * sqsize + sqsize // 2)
                    pygame.draw.line(screen, color, iPos, fPos, line_width)
                # Return the winning player number    
                return self.squares[row][0]

        # Check for descending diagonal win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            # If 'show' is True, draw a line to visualize the winning pattern
            if show:
                color = circ_color if self.squares[1][1] == 2 else cross_color
                iPos = (20, 20)
                fPos = (width - 20, height - 20)
                pygame.draw.line(screen, color, iPos, fPos, cross_width)
            # Return the winning player number    
            return self.squares[1][1]

        # Check for ascending diagonal win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            # If 'show' is True, draw a line to visualize the winning pattern
            if show:
                color = circ_color if self.squares[1][1] == 2 else cross_color
                iPos = (20, height - 20)
                fPos = (width - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, cross_width)
            # Return the winning player number    
            return self.squares[1][1]
        

        # If no win yet, return 0
        return 0

    def mark_sqr(self,row,col,player): #Method to mark a square on the board with the player's symbol
        self.squares[row][col] = player# Mark the square at the given row and column with the player's symbol
        self.marked_sqrs += 1# Increment the count of marked squares by 1

    def empty_sqr(self,row,col):
        return self.squares[row][col] == 0 # checking if the board is empty or not
    
    def get_empty_sqrs(self): # Iterate through each square on the board
        empty_sqrs = []
        for row in range(rows):
            for col in range(cols):
                # Check if the square at (row, col) is empty
                if self.empty_sqr(row, col):
                    # If empty, add the coordinates to the list of empty squares
                    empty_sqrs.append( (row, col) )
        
        return empty_sqrs
    
    def isfull(self):
        return self.marked_sqrs == 9 # Checks if all squares on the board are marked, indicating a full board

    def isempty(self):
        return self.marked_sqrs == 0 # Checks if no squares on the board are marked, indicating an empty board

class AI:

    def __init__(self, level=1, player=2):
        self.level = level # Set the AI's level to the specified level (default: 1)
        self.player = player # Set the AI's player number to the specified player (default: 2)

    # Random move generation method

    def rnd(self, board):# Method to generate a random move for the AI on the provided board
        empty_sqrs = board.get_empty_sqrs()# Get a list of empty squares on the board
        idx = random.randrange(0, len(empty_sqrs))# Generate a random index within the range of available empty squares

        return empty_sqrs[idx] # Return a randomly chosen empty square (row, col) for the AI's move

    # minimax algorithm for AI move selection
    def minimax(self, board, maximizing): # Method implementing the minimax algorithm for optimal move selection
        
        # Check for terminal cases (win, lose, draw)
        case = board.final_state()# Check the final state of the board

        # If player 1 wins, return evaluation 1 and no move
        if case == 1:
            return 1, None # Evaluation for player 1 wins, no move needed

        # If player 2 wins, return evaluation -1 and no move
        if case == 2:
            return -1, None

        # If the game is a draw, return evaluation 0 and no move
        elif board.isfull():
            return 0, None

        # If maximizing player's turn
        if maximizing:
            max_eval = -100 # Set initial maximum evaluation to a low value
            best_move = None # Initialize the best move variable as None
            empty_sqrs = board.get_empty_sqrs() # Get a list of empty squares on the board

            # Iterate through available empty squares
            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)# Create a copy of the board
                temp_board.mark_sqr(row, col, 1)# Mark the square for player 1
                eval = self.minimax(temp_board, False)[0]# Recursive call for opponent's turn evaluation
                if eval > max_eval: # Check if the evaluation is better than the current maximum
                    max_eval = eval # Update maximum evaluation
                    best_move = (row, col) # Update the best move with the current square

            return max_eval, best_move # Return the maximum evaluation and the best move for maximizing player

        elif not maximizing:
            min_eval = 100 # Set initial minimum evaluation to a high value
            best_move = None # Initialize the best move variable as None
            empty_sqrs = board.get_empty_sqrs() # Get a list of empty squares on the board

            # Iterate through available empty squares
            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board) # Create a copy of the board
                temp_board.mark_sqr(row, col, self.player) # Mark the square for the AI player
                eval = self.minimax(temp_board, True)[0] # Mark the square for the AI player
                if eval < min_eval: # Check if the evaluation is better than the current minimum
                    min_eval = eval # Update minimum evaluation
                    best_move = (row, col) # Update the best move with the current square

            return min_eval, best_move

    # --- MAIN EVAL ---

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            eval, move = self.minimax(main_board, False)

        print(f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')

        return move # row, col

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        if pl == 2:
            self.player = 2 # for now 1=cross 2=circle
        else:
            self.player = 1 # for now 1=cross 2=circle    
        if gmd == 0 or gmd == 1:
            self.gamemode = 'ai' #Ai
        else:
            self.gamemode = 'pvp' #pvp 
        self.running = True
        self.show_lines()# When a Game object is created, it calls the show_lines method to set up the grid

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)# Mark the square on the board with the player's symbol
        self.draw_fig(row, col)# Draw the figure (symbol) on the GUI interface at the specified row and column
        self.next_turn()# Proceed to the next turn, switching the player

    def show_lines(self):
        screen.fill( bg_colour )
        #vertical
        pygame.draw.line(screen,line_color, (sqsize,0), (sqsize, height), line_width)# Left vertical line start(200,0) End (200,600)
        pygame.draw.line(screen,line_color, (width - sqsize,0), (width - sqsize, height), line_width)# right vertical line start(400,0) End (400,600)

        #horizontal
        pygame.draw.line(screen,line_color, (0,sqsize), (width, sqsize), line_width)# Left horizontal line start(0,200) End (600,200)
        pygame.draw.line(screen,line_color, (0, height - sqsize,), (width, width - sqsize,), line_width)# right horizontal line start(0,400) End (600,400)

    def draw_fig(self, row, col):
        if self.player == 1:
            #draw a cross at the calculated center position
            #Descending diagonal line (from top-left to bottom-right inside the square)
            start_desc = (col * sqsize + offset, row * sqsize + offset)
            end_desc = (col * sqsize + sqsize - offset, row * sqsize + sqsize - offset)
            pygame.draw.line(screen, cross_color, start_desc, end_desc, cross_width)
            #Ascending diagonal line (from bottom-left to top-right inside the square)
            start_asc = (col * sqsize + offset, row * sqsize + sqsize - offset)
            end_asc = (col * sqsize + sqsize - offset, row * sqsize + offset)
            pygame.draw.line(screen, cross_color, start_asc, end_asc, cross_width)
            
        elif self.player == 2:
            # Draw a circle at the calculated center position
            center = (col * sqsize + sqsize // 2, row * sqsize + sqsize // 2)#(100,100)(300,100)(450,100)
            pygame.draw.circle(screen, circ_color, center, radius, circ_width)

    def next_turn(self):
        self.player = self.player % 2 +1 # Toggle the player between 1 and 2 for the next turn

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    # Inside your Game class

    # Add these variables to keep track of blinking animation
    blink_interval = 60  # Number of frames to show each message
    blink_counter = 0  # Counter to manage blinking interval
    show_message = True  # Flag to toggle message visibility

    # Modify the isover method to include blinking animation
    def isover(self):
        winning_message_1 = "Player 1 wins!"
        winning_message_2 = "Player 2 wins!"
        draw_message = "It's a draw!"

        win_state = self.board.final_state(show=True)

        if win_state == 1 and pl == 1:
            self.game_message = winning_message_1
            return True
        elif win_state == 1 and pl == 2:
            self.game_message = winning_message_2
            return True
        # Add similar conditions for other win/draw states...

        # Implement blinking effect for the message
        if self.board.isfull() or win_state != 0:  # If the game is over
            self.blink_counter += 1
            if self.blink_counter % self.blink_interval == 0:
                self.show_message = not self.show_message  # Toggle message visibility
            if self.show_message:
                # Display the message if it's time to show
                if win_state != 0:
                    self.game_message = winning_message_1 if pl == 1 else winning_message_2
                else:
                    self.game_message = draw_message
            else:
                self.game_message = ""  # Hide the message during blinking

            return True

        self.blink_counter = 0  # Reset blink counter if the game is not over
        return False


def main():

    #object of Game class
    game = Game()
    board = game.board
    ai = game.ai

    #main loop
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:# Check if the quit event (closing the window) is triggered
                pygame.quit()# Quit Pygame
                sys.exit()# Exit the program
            
            # Check the integer value and perform actions based on its value
            if gmd == 0:
                ai.level = 0
            elif gmd == 1:
                ai.level = 1
            elif gmd == 3:
                game.gamemode = 'PvP'    

            # keydown event
            if event.type == pygame.KEYDOWN:
                # r-restart
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos  # Get the position of the mouse click (x, y)
                row = pos[1] // sqsize  # Calculate the row number by dividing the y-coordinate by sqsize(200)
                col = pos[0] // sqsize  # Calculate the column number by dividing the x-coordinate by sqsize(200)

                # human mark sqr
                if board.empty_sqr(row, col) and game.running:
                    # Check if the selected square on the board is empty and the game is running
                    # Make a move on the board if the selected square is empty and the game is ongoing
                    game.make_move(row, col)

                    if game.isover():
                        # Check if the game is over after the move
                        game.running = False # Set the game's running status to False as the game is over

                        # Display the game message using Pygame.font module
                        font = pygame.font.SysFont("freesansbold", 40)
                        text = font.render(game.game_message, True, (0, 0, 0))
                        text_rect = text.get_rect()
                        text_rect.center = (width // 2, height // 2)
                        screen.blit(text, text_rect)
                        pygame.display.update()



        # AI initial call
        if game.gamemode == 'ai' and game.player == ai.player and  game.running:
            # update the screen
            pygame.display.update()

            # eval
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.isover():
                game.running = False

                # Display the game message using Pygame.font module
                font = pygame.font.SysFont("freesansbold", 40)
                text = font.render(game.game_message, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = (width // 2, height // 2)
                screen.blit(text, text_rect)
                pygame.display.update()

        pygame.display.update() # Update the contents of the display 
        
main()