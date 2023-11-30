import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Versatile Buttons")

# Define button properties
button_height = 50
button_margin = 20  # Adjust this value to control the gap between buttons
button_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
button_texts = ["Button 1", "Button 2", "Button 3", "Button 4"]

# Function to draw buttons
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(screen, color, (x, y, width, height))

    # Optional: Add text to the button
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Function to create buttons
def create_buttons(screen_width, screen_height, button_height, button_margin, button_colors, button_texts):
    num_buttons = len(button_texts)
    button_width = (screen_width - (num_buttons + 1) * button_margin) // num_buttons

    # Draw buttons at the bottom of the screen
    buttons = []
    for i in range(num_buttons):
        button_x = i * (button_width + button_margin) + button_margin
        button_y = screen_height - button_height - button_margin

        draw_button(button_x, button_y, button_width, button_height, button_colors[i], button_texts[i])
        buttons.append((i, button_x, button_y, button_width, button_height))

    return buttons

# Main game loop
buttons = create_buttons(screen_width, screen_height, button_height, button_margin, button_colors, button_texts)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Check which button was clicked
            for i, button_x, button_y, button_width, button_height in buttons:
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    print(f"Button {i + 1} clicked!")

    # Update the display
    pygame.display.flip()
