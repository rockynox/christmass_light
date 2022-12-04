import time

from main import village
from neopixelwrapper import pixels

colors = [
    (255, 0, 0, 0),
    (0, 255, 0, 0),
    (0, 0, 255, 0),
    (0, 0, 0, 255),
]

try:
    while True:
        for color in colors:
            for door in village:
                door.light(color)
                pixels.show()
                time.sleep(1)
finally:
    pixels.fill((0, 0, 0, 0))
    pixels.show()
