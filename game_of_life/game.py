# To create & start using python venv:
#       python -m venv venv
#       source venv/bin/activate

# Intall specific modules with pip:
# f.e.:   pip install pygame

# Requirements
# 1. Make simulation real time
# 2. Add pause / resume logic
# 3. Add save / load logic

# High-level logic
# 1. Create and init the simulation grid (Connect with tick)
# 2. Start the simulation with a tick interval of <n> seconds
# 3. At each tick:
#   3.1. Update the grid - loop over each element of the board
#   3.2. Render new generation

# General approach
# 1. Plan & write down the general workflow
#  1.1. Define Input&Output
#  1.2. Consider adding validation
# 2. Separate the main algorithms / actors in the code. Try to abstract as much common code as possible
# 3. Define communication between the objects
# 4. List the patterns you could apply
# 5. Build PoCs (Proof of concepts). Try to separate implementation of specific steps. Prepare smaller modules
#    and combine them into a complete application
# 6. Refine if needed

# Deadline - 15th of December 2023
# Mail with:
# 1. short screen recording demonstrating the new features
# 2. Linked code
# 3. Short description of the changes. Which design patterns you used and how you applied them.

import pygame
import numpy as np
import time
import json
from abc import ABC, abstractmethod

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Game state
game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)
font = pygame.font.Font(None, 24)

# Button properties
button_height, button_margin = 50, 20
button_texts = ["Start", "Stop", "Save", "Load"]

# Refactored function to draw single button
def draw_button(x, y, width, height, text):
    pygame.draw.rect(screen, green, (x, y, width, height))
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Function to create multiple buttons at once
def create_buttons(screen_width, screen_height, button_height, button_margin, button_texts):
    num_buttons = len(button_texts)
    button_width = (screen_width - (num_buttons + 1) * button_margin) // num_buttons
    # Draw buttons at the bottom of the screen
    buttons = []
    for i in range(num_buttons):
        button_x = i * (button_width + button_margin) + button_margin
        button_y = screen_height - button_height - button_margin

        draw_button(button_x, button_y, button_width, button_height, button_texts[i])
        buttons.append((i, button_x, button_y, button_width, button_height))

    return buttons


def draw_grid():
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, gray, cell, 1)

def next_generation():
    global game_state
    new_state = np.copy(game_state)

    for y in range(n_cells_y):
        for x in range(n_cells_x):
            n_neighbors = game_state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]

            if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_state[x, y] = 0
            elif game_state[x, y] == 0 and n_neighbors == 3:
                new_state[x, y] = 1

    game_state = new_state

def draw_cells():
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(screen, black, cell)


##SAVING & LOADING

class FileReader(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass

class GameStateAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abstractmethod
    def get_game_state(self) -> np.ndarray:
        pass

# Specific implementation of the adpater to read JSON Source data
class JSONGameStateAdapter(GameStateAdapter):
    def get_game_state(self):
        try:
            data = json.loads(self.data_source.read())
            updated_game_state = np.array(data)
            return updated_game_state
        except FileNotFoundError:
            print(f"File not found: {self.data_source.file_name}")
            return None
        except json.JSONDecodeError:
            print(f"Wrong file format: {self.data_source.file_name}")
            return None

class JSONReader(FileReader):
    def read(self):
        try:
            with open(self.file_name, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
            return ''

class JSONGameStateReader:
    def __init__(self, file_name):
        self.json_reader = JSONReader(file_name)
        self.json_adapter = JSONGameStateAdapter(self.json_reader)

    def load_game_state(self, global_game_state):
        updated_game_state = self.json_adapter.get_game_state()
        if updated_game_state is not None:
            np.copyto(global_game_state, updated_game_state)
            print("Game loaded")
        else:
            print("Loading failed")



def save_to_json(game_state):
    game_state_list = game_state.tolist()
    with open('game_state.json', 'w') as json_file:
        json.dump(game_state_list, json_file)
    print("Game saved to JSON")



# Define state class
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ClockState:
    def __init__(self):
        self.state = False
        self.observers = []

    def start_clock(self):
        self.state = True
        self.observers = []

    def stop_clock(self):
        self.state = False
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class ClockTicks(Observer):
    def __init__(self):
        self.number_of_ticks = 0
    def add(self):
        self.number_of_ticks += 1
    def get_ticks(self):
        return self.number_of_ticks
    def display(self):
        print(f"Time: {self.number_of_ticks}")
    def update(self, subject):
        if subject.state:
            self.add()
            self.display()


#Update game every 1 second
def update_next_generation(clock_state, last_update_time, clock_ticks):
    current_time = time.time()
    if clock_state.state and (current_time - last_update_time >= 1):
        next_generation()
        clock_ticks.add()
        return current_time  # Update the timer when next_generation is executed
    return last_update_time

def display_ticks():
    text = font.render(f"Ticks: {clock_ticks.get_ticks()}", True, green)
    text_rect = text.get_rect(topright=(width - 10, 10))
    screen.blit(text, text_rect)

#Main game loop
running = True
clock_state = ClockState()  # State
clock_ticks = ClockTicks()
last_update_time = time.time()  # time from last update
json_game_state_reader = JSONGameStateReader('game_state.json')

while running:
    screen.fill(white)
    draw_grid()
    draw_cells()
    display_ticks()
    buttons = create_buttons(width, height, button_height, button_margin, button_texts)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Check which button was clicked
            for i, button_x, button_y, button_width, button_height in buttons:
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    if i == 0: #Start button
                        clock_state.start_clock()
                    elif i == 1: #Pause bttn
                        clock_state.stop_clock()
                    elif i == 2: #Save bttn
                        save_to_json(game_state)
                    elif i == 3: #Load bttn
                        json_game_state_reader.load_game_state(game_state)
                else:
                    x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                    game_state[x, y] = not game_state[x, y]

    last_update_time = update_next_generation(clock_state, last_update_time, clock_ticks)


pygame.quit()

