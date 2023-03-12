import logging
import sys
from datetime import datetime
from itertools import chain

from door import Door
from logger import setup_logger
from neopixelwrapper import pixels
from tools import get_now, get_sun_times

village = [
    Door(1, list(chain(range(0, 5), range(5, 9)))),
    Door(5, list(range(9, 18))),

    Door(14, list(range(18, 27))),
    Door(3, list(range(27, 34))),  # -2 Led dehors

    Door(17, list(range(36, 45))),
    Door(6, list(range(45, 54))),
    Door(9, list(range(45, 54))),

    Door(11, list(range(54, 63))),
    #Door(11, list(range(63, 72))),
    Door(19, list(range(63, 72))),

    Door(21, list(range(72, 78))),
    Door(7, list(range(78, 84))),
    Door(15, list(range(84, 90))),
]

if __name__ == '__main__':
    setup_logger(logging.DEBUG)
    try:
        # timer = Timer()
        current_day = None

        while True:
            # timer.update()
            current_time = get_now()

            if current_time.day != current_day:
                current_day = current_time.day
                sun_times = get_sun_times()
                for door in village:
                    door.change_day(current_time, sun_times)

            for door in village:
                door.update_door_leds_state(current_time)
            pixels.show()
    finally:
        pixels.fill((0, 0, 0, 0))
        pixels.show()
