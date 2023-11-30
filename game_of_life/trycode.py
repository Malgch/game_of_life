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

# Set up buttons
buttons = ["Button 1", "Button 2", "Button 3", "Button 4"]
button_rects = []


# Function to draw a button
def draw_button(x, y, width, height, text):
    pygame.draw.rect(screen, gray, (x, y, width, height))

    # Render the text
    text_rendered = font.render(text, True, white)

    # Get the text rectangle
    text_rect = text_rendered.get_rect()

    # Center the text on the button
    text_rect.center = (x + width // 2, y + height // 2)

    # Draw the text on the screen
    screen.blit(text_rendered, text_rect)

    # Save the button rectangle for future interaction checks
    button_rects.append(pygame.Rect(x, y, width, height))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Draw the four buttons
    button_width, button_height = 150, 50
    button_margin = 20

    for i, button_text in enumerate(buttons):
        x = (width - button_width * 2 - button_margin) // 2 + (i % 2) * (button_width + button_margin)
        y = (height - button_height * 2 - button_margin) // 2 + (i // 2) * (button_height + button_margin)
        draw_button(x, y, button_width, button_height, button_text)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

    # Example interaction check: print the button name when clicked
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clicked_buttons = [i for i, rect in enumerate(button_rects) if rect.collidepoint(mouse_x, mouse_y)]

    for button_index in clicked_buttons:
        print(f"Button '{buttons[button_index]}' clicked!")
