import sys
import termios
import fcntl
import os
import time
import pyfirmata

board = pyfirmata.Arduino('/dev/cu.usbmodem14201')
servo_pin = board.get_pin('d:9:s')

def get_pulse_width(timeout=.1, default=1500):
    """
    Get pulse width from user input (arrow keys) with optional timeout and default value.
    """
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        # Set non-blocking mode for stdin
        fcntl.fcntl(sys.stdin, fcntl.F_SETFL, os.O_NONBLOCK)
        # Get start time
        start_time = time.time()
        # Initialize pulse width to default value
        pulse_width = default
        # Set initial increment value and direction
        increment = 10
        direction = None
        while True:
            # Check if timeout has been reached
            if time.time() - start_time > timeout:
                break
            try:
                # Read one character from stdin
                c = sys.stdin.read(1)
                if c == '\x1b':  # If first character is an escape sequence (arrow key)
                    # Read the next two characters (arrow key code)
                    c2 = sys.stdin.read(1)
                    c3 = sys.stdin.read(1)
                    if c2 == '[':
                        if c3 == 'A':  # Up arrow key
                            direction = 'up'
                        elif c3 == 'B':  # Down arrow key
                            direction = 'down'
                        # Reset increment to initial value
                        increment = 10
                elif c == '':  # No input
                    pass
                else:  # Any other input exits the loop
                    break
            except IOError:
                pass
            # If direction is up or down, ramp up or down the pulse width
            if direction == 'up':
                pulse_width = min(pulse_width + increment, 2000)
                increment = min(increment + 5, 100)
            elif direction == 'down':
                pulse_width = max(pulse_width - increment, 1000)
                increment = min(increment + 5, 100)
            # Send updated pulse width to servo
            servo_pin.write(pulse_width / 20000.0)
            time.sleep(0.01)
        # Reset servo to default position
        servo_pin.write(default / 20000.0)
        # Return final pulse width
        return pulse_width
    finally:
        # Restore original stdin settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
