import pyfirmata
import time

# Set up the board
board = pyfirmata.Arduino('/dev/tty.usbmodem101')

# Define pins
servo_pin = board.get_pin('d:13:s')

# Set the speed of the sweep (in seconds per step)
sweep_speed = 0.05

# Sweep the servo back and forth continuously
while True:
    # Sweep from 0 to 180 degrees
    for angle in range(0, 181, 1):
        servo_pin.write(angle)
        time.sleep(sweep_speed)
    
    # Sweep from 180 to 0 degrees
    for angle in range(180, -1, -1):
        servo_pin.write(angle)
        time.sleep(sweep_speed)

# Close the board connection
board.exit()
