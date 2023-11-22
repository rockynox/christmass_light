import logging

from christmas_village.door import Door
from common.logger import setup_logger
from common.neopixelwrapper import pixels
from common.tools import get_now, get_sun_times

village = [
    Door(1, list(range(0, 9))),
    Door(5, list(range(9, 18))),

    Door(14, list(range(18, 27))),
    Door(3, list(range(27, 36))),

    Door(17, list(range(36, 42))),
    Door(6, list(range(42, 48))),
    Door(9, list(range(48, 54))),

    Door(11, list(range(54, 63))),
    Door(19, list(range(63, 72))),

    Door(21, list(range(72, 78))),
    Door(7, list(range(78, 84))),
    Door(15, list(range(84, 90))),
]

if __name__ == '__main__':
    setup_logger(logging.DEBUG)
    try:
        current_day = None

        while True:
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
