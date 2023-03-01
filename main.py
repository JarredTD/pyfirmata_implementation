import pygame
import pyfirmata
import time

# Define the port and board
port = '/dev/tty.usbemoden101'  # replace with your board's port
board = pyfirmata.Arduino(port)

# Define the pin
speed_pin = board.get_pin('d:13:o')

# Define constants
UP_KEY = pygame.K_w
DOWN_KEY = pygame.K_s
UP_START = 1650
UP_STOP = 2000
UP_STEP = 1
DOWN_START = 1450
DOWN_STOP = 1000
DOWN_STEP = 1

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Set up font
font = pygame.font.Font(None, 36)

# Set up initial values
mode = None
value = 1500

# Run loop
running = True
while running:
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Handle key presses
            if event.key == UP_KEY:
                mode = 'up'
                value = UP_START
            elif event.key == DOWN_KEY:
                mode = 'down'
                value = DOWN_START
        elif event.type == pygame.KEYUP:
            # Handle key releases
            if event.key == UP_KEY or event.key == DOWN_KEY:
                mode = None
                value = 1500

    # Update value based on mode
    if mode == 'up':
        if value < UP_STOP:
            value += UP_STEP
    elif mode == 'down':
        if value > DOWN_STOP:
            value -= DOWN_STEP

    # Draw to screen
    screen.fill((255, 255, 255))
    text = font.render(f'Value: {value}', True, (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    speed_pin.write(value)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
# Close the board connection
board.exit()
