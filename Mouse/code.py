import board
import digitalio
import neopixel
import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)
pixel.fill((0, 0, 255)) #Set pixel blue

while True:
    
    # if not button.value:
    #     print("Button press")
    #     pixel.fill((255, 0, 0)) #Set pixel red
    # else:
    #     print("Button release")
    #     pixel.fill((0, 0, 0)) #Set pixel off
    
    print("Mouse")
    mouse.move(x=1)
    mouse.move(x=-1)
    time.sleep(30)
    pixel.fill((0, 255, 0)) #Set pixel green
    time.sleep(1)
    pixel.fill((0, 0, 0)) #Set pixel off
    
