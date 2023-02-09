from pyfirmata import ArduinoMega, util

board = ArduinoMega('/dev/tty.usbserial-A6008rIF')
board.digital[13].write(0)

# it = util.Iterator(board)
# it.start()
# board.analog[0].enable_reporting()
# board.analog[0].read()