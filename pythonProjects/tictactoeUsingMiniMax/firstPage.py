import pygame  # Pygame library for handling game functionality and graphics.
import sys  # Module providing access to some variables used or maintained by the Python interpreter.
import subprocess  # Module to spawn new processes, here used to execute external commands or scripts.
import pyautogui  # PyAutoGUI library for programmatically controlling the mouse and keyboard.
import time  # Module providing various time-related functions.
from constants import *  # Importing constants from a custom module for use throughout the script.
# The 'constants' module is containing design constants for use in the script.


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height)) # Create a window display with dimensions (width, height) using Pygame.
pygame.display.set_caption("Tic Tac Toe") # Set the title or caption of the Pygame window to "Tic Tac Toe".

# Function to open the Tic Tac Toe game
def open_tic_tac_toe(button):
    # Check which button was clicked and set the game mode accordingly
    if button == "PvP":
        mode = 3 # Set mode to 3 for Player vs Player

    subprocess.Popen(["python", "tictactoeAi.py", str(mode)])# Execute the Tic Tac Toe game subprocess with the selected mode
    time.sleep(5)  # Wait for the window to open (adjust the delay if needed)
    
# Function to open the Tic Tac Toe game
def open_second_page(button):
    # Check which button was clicked and set the game mode accordingly
    if button == "AI (Hard)":
        mode = 1
    elif button == "AI (Easy)":  # Handling for "AI (Easy)" button
        mode = 0
    #opening the second page and sending vlaue with it    
    subprocess.Popen(["python", "secondPage.py", str(mode)])# Execute the Tic Tac Toe game subprocess with the selected mode
    time.sleep(5)  # Wait for the window to open (adjust the delay if needed)

# Function to draw rectangular-bordered buttons
def draw_button(text, pos):
    font = pygame.font.Font(None, 36) # Set the font for the button text to size 36 using the default system font.
    text_render = font.render(text, True, (0, 0, 0)) # Render the text using the defined font, with anti-aliasing, in black color (0, 0, 0).
    text_rect = text_render.get_rect(center=pos)# Get the rectangle representing the text surface and position it at the center of the button.
    
    rect_width, rect_height = 180, 50 #Define the width and height of the rectangular border for the button.

    # Draw a rectangular border on the screen using the defined position, width, height, and line color.
    #draw a red rectangle at coordinates (300, 300) with a width of 100 and a height of 60. 
    #The rectangle will have a border of 4 pixels in thickness.
    pygame.draw.rect(screen, line_color, (pos[0] - rect_width // 2, pos[1] - rect_height // 2, rect_width, rect_height), 4)
    
    screen.blit(text_render, text_rect)# Blit (copy) the rendered text onto the screen at the specified rectangle position.


# Function to draw the title
def draw_title():
    font = pygame.font.Font(None, 48) # Set the font for the title text to size 48 using the default system font.
    title_text = font.render("Select your game mode", True, (0, 0, 0)) # Render the title text using the defined font, with anti-aliasing, in black color (0, 0, 0).
    #Anti-aliasing is a technique used in graphics to reduce visual distortion, particularly in curved or diagonal lines and edges.
    
    title_rect = title_text.get_rect(center=(width // 2, height // 4))# Get the rectangle representing the text surface and position it at the center of the screen's top part.
    screen.blit(title_text, title_rect)# Blit (copy) the rendered title text onto the screen at the specified rectangle position.

# Function to check button clicks
def check_button_click(mouse_pos):
    button_positions = {
        # Dictionary defining button positions and their respective coordinates
        "PvP": (width // 2, height // 2),
        "AI (Easy)": (width // 2, height // 2 + 100),
        "AI (Hard)": (width // 2, height // 2 + 200)
    }

    # Iterate through each button position in the dictionary
    # dictionary means 
    for button, pos in button_positions.items():
        # Get width and height values for the rectangular boundaries of the button
        rect_width, rect_height = 180, 50
        
        # Check if mouse is within the rectangular boundary
        if (pos[0] - rect_width // 2 <= mouse_pos[0] <= pos[0] + rect_width // 2 and
            pos[1] - rect_height // 2 <= mouse_pos[1] <= pos[1] + rect_height // 2):
            # Perform an action associated with the clicked button
            if button == "PvP":
                open_tic_tac_toe(button)#button is pvp then go directly to the main page
            else:
                open_second_page(button)#go to the second page and chose player then it will re direct to the main page

# Game loop
def main():
    while True:
        screen.fill(bg_colour)# Fill the screen with the specified background color


        # # Draw the title text on the screen
        draw_title()

        # Draw buttons for Player vs Player and AI modes at specific positions on the screen
        draw_button("PvP", (width // 2, height // 2))
        draw_button("AI (Easy)", (width // 2, height // 2 + 100))
        draw_button("AI (Hard)", (width // 2, height // 2 + 200))

        # Check and handle events such as window close or mouse click
        for event in pygame.event.get():
            # Check if the user wants to quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if there is a mouse button click event    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position when a click occurs
                mouse_pos = pygame.mouse.get_pos()
                # Check which button was clicked and take action accordingly
                check_button_click(mouse_pos)
        # Update the display to show the changes
        pygame.display.update()

if __name__ == "__main__":
    main()
