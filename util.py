import sys
import termios
import tty

def set_terminal_raw():
    # get the current terminal settings
    old_settings = termios.tcgetattr(sys.stdin)
    # set the terminal to raw mode
    tty.setraw(sys.stdin)
    return old_settings

def get_input_byte():
    # read a single byte from the keyboard
    byte = sys.stdin.buffer.read(1)
    # convert byte to byte string
    byte_str = bytes(byte)
    return byte_str

def restore_terminal_settings(old_settings):
    # restore the original terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
