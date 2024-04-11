import sys
import time

sys.path.insert(0, '/home/pi/christmass_light')
from common.neopixelwrapper import pixels

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 255),
]

try:
    while True:
        for color in colors:
            for door in range(0, 12):
                pixels.fill((250, 83, 10))
                pixels[door] = (255, 255, 255)
                pixels.show()
                print(f"Light door {door}")
                time.sleep(0.9)
finally:
    pixels.fill((0, 0, 0, 0))
    pixels.show()
