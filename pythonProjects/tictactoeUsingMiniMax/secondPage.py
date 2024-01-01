import os
import pygame
import sys
import subprocess
import time
from constants import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))# Set up the game window with specified dimensions
pygame.display.set_caption("Select First Move")# Set the title of the game window

# Check if command-line arguments were passed
if len(sys.argv) > 1:
    gmd = int(sys.argv[1])# Convert the first argument to an integer (mode selection)
else:
    gmd = 0  # Default value if no mode argument is passed

# Redefine sqsize to adjust button size
sqsize = 100  # Adjust this value to change button size

# Function to open the Tic Tac Toe game
def open_tic_tac_toe(button):
    # Check which button was clicked and assign player order
    if button == "Me":
        player_first = 1 # Player goes first
    elif button == "AI":
        player_first = 2 # AI goes first

    # Combining game mode and player order
    values_to_pass = f"{gmd} {player_first}"

    subprocess.Popen(["python", "tictactoeAi.py", values_to_pass])
    time.sleep(5)  # Wait for the window to open (adjust the delay if needed)

    os._exit(0)# Terminate the current process (closes the current script execution)

# Function to draw rectangular-bordered buttons
def draw_button(text, pos):
    font = pygame.font.Font(None, 36)
    text_render = font.render(text, True, (0, 0, 0))
    text_rect = text_render.get_rect(center=pos)
    
    # Draw rectangular border with adjusted size
    rect_width, rect_height = sqsize, sqsize // 3  # Adjusted button size
    pygame.draw.rect(screen, line_color, (pos[0] - rect_width // 2, pos[1] - rect_height // 2, rect_width, rect_height), 4)
    
    screen.blit(text_render, text_rect)

# Function to draw the title
def draw_title():
    font = pygame.font.Font(None, 48)
    title_text = font.render("Select who will give the first move?", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(width // 2, height // 4))
    screen.blit(title_text, title_rect)

# Function to check button clicks
def check_button_click(mouse_pos):
    button_positions = {
        "Me": (width // 2, height // 2 - sqsize // 2),
        "AI": (width // 2, height // 2 + sqsize // 2),
    }

    for button, pos in button_positions.items():
        rect_width, rect_height = sqsize, sqsize // 3
        
        # Check if mouse is within the rectangular boundary
        if (pos[0] - rect_width // 2 <= mouse_pos[0] <= pos[0] + rect_width // 2 and
            pos[1] - rect_height // 2 <= mouse_pos[1] <= pos[1] + rect_height // 2):
            open_tic_tac_toe(button)

# Function to draw buttons after the title
def draw_interface():
    # Draw title
    draw_title()

    # Draw buttons
    draw_button("Me", (width // 2, height // 2 - sqsize // 2))
    draw_button("AI", (width // 2, height // 2 + sqsize // 2))

# Game loop
def main():
    while True:
        screen.fill(bg_colour)

        # Draw interface components
        draw_interface()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                check_button_click(mouse_pos)

        pygame.display.update()

if __name__ == "__main__":
    main()
