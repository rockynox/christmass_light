from itertools import chain

from door import Door
from neopixelwrapper import pixels
from tools import get_now, get_sun_times, Timer

if __name__ == '__main__':
    timer = Timer()
    current_time = get_now()
    current_day = None
    village = [
        Door(1, list(chain(range(0, 5), range(5, 9)))),
        Door(3, range(27, 36)),
        Door(5, range(9, 18)),
        Door(7, range(78, 84)),
        Door(9, range(45, 54)),
        Door(11, range(54, 63)),
        Door(13, range(18, 27)),
        Door(15, range(84, 90)),
        Door(17, range(36, 45)),
        Door(19, range(63, 71)),
        # Door(21, range(72, 78)),
        Door(29, range(72, 78))  # TEST DOOR
    ]

    while True:
        # time.sleep(0.1)  # In sec
        timer.update()

        if current_time.day != current_day:
            current_day = current_time.day
            sun_times = get_sun_times()
            for door in village:
                door.change_day(current_time, sun_times)

        for door in village:
            door.update_door_leds_state(current_time)
        pixels.show()
