# import pyfirmata
# import time
import util

# # Set up the Arduino board
# board = pyfirmata.Arduino('/dev/cu.usbmodem101') # replace 'COM3' with the appropriate port for your board
# board.digital[13].mode = pyfirmata.OUTPUT # set the digital pin 13 (built-in LED) as an output

util.set_terminal_raw()
byte_str = ''
while (byte_str != b'\x11'):
    byte_str = util.get_input_byte()
    print(byte_str)


util.restore_terminal_settings()