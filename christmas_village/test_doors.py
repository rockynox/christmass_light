import time

from christmas_village.__main__ import village
from common.neopixelwrapper import pixels

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
                print(f"Light door {door.day_number} with range {list(door.led_range)}")
                time.sleep(1)
finally:
    pixels.fill((0, 0, 0, 0))
    pixels.show()
