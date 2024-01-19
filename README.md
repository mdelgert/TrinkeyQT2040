# TrinkeyQT2040
https://circuitpython.org/board/adafruit_qt2040_trinkey/
https://learn.adafruit.com/adafruit-trinkey-qt2040/u2if-python-example
https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse

# Example for CircuitPython 8.2.9
https://downloads.circuitpython.org/bin/adafruit_qt2040_trinkey/en_US/adafruit-circuitpython-adafruit_qt2040_trinkey-en_US-8.2.9.uf2

# Delete everything from REPL
import storage
storage.erase_filesystem()

# Delete boot.py from REPL
import os
os.remove("boot.py")