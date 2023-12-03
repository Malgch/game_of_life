import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Clock")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Get the current time
    current_time = pygame.time.get_ticks()

    # Convert milliseconds to seconds
    seconds = current_time // 1000

    # Calculate minutes and seconds
    minutes = seconds // 60
    seconds %= 60

    # Format the time as text
    time_text = f"{minutes:02}:{seconds:02}"

    # Create a font object
    font = pygame.font.Font(None, 36)

    # Render the text
    text = font.render(time_text, True, white)

    # Get the text rectangle
    text_rect = text.get_rect()

    # Center the text on the screen
    text_rect.center = (width // 2, height // 2)

    # Draw the text on the screen
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Buttons")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (169, 169, 169)

# Set up font
font = pygame.font.Font(None, 36)



# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)



    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
