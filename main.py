import pyfirmata
import time
import Getch

# Set up the Arduino board
board = pyfirmata.Arduino('/dev/cu.usbmodem101') # replace 'COM3' with the appropriate port for your board
board.digital[13].mode = pyfirmata.OUTPUT # set the digital pin 13 (built-in LED) as an output

while True:
    output = Getch.get_pulse_width(.1)
    board.digital[13].write(output) # turn the LED on
    print(output)