import pyfirmata
import time

# Set up the Arduino board
board = pyfirmata.Arduino('devtty') # replace 'COM3' with the appropriate port for your board
board.digital[13].mode = pyfirmata.OUTPUT # set the digital pin 13 (built-in LED) as an output

# Blink the LED rapidly
count = 0
while True:
    board.digital[13].write(1) # turn the LED on
    time.sleep(0.1) # wait for 0.1 seconds
    board.digital[13].write(0) # turn the LED off
    time.sleep(0.1) # wait for 0.1 seconds
    print(f"Iteration: {count}")
    count+=1