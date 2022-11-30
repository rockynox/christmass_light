import random
from datetime import time, datetime

from neopixelwrapper import WHITE_INDEX, RED_INDEX, pixels


# FancyLED: For color correction

def get_morning_times(sun_time):
    morning_light_up = time(random.randint(6, 7), random.randint(0, 59))
    morning_shutdown = time(random.randint(7, sun_time["sunrise"].hour + 1), random.randint(0, 59))
    return [morning_light_up, morning_shutdown]


def get_evening_times(sun_time):
    evening_light_up = time(random.randint(sun_time["sunset"].hour - 1, 19), random.randint(0, 59))
    evening_shutdown = time(random.randint(21, 23), random.randint(0, 59))
    return [evening_light_up, evening_shutdown]


class Door:
    def __init__(self, day_number: int, led_range: [int]):
        self.day_number = day_number
        self.led_range = led_range
        self.morning_times = None
        self.evening_times = None
        self.is_door_day = False

        self.current_celebration_color = [0, 0, 0, 250]
        self.celebration_increasing_color = RED_INDEX
        self.celebration_decreasing_color = WHITE_INDEX

    def should_light(self, current_datetime: datetime):
        if self.evening_times[0] < current_datetime.time() < self.evening_times[1]:
            return True
        elif self.morning_times[0] < current_datetime.time() < self.morning_times[1]:
            return False

    def update_door_leds_state(self, current_datetime: datetime):
        door_leds = {}
        if self.should_light(current_datetime):
            if self.is_door_day:
                for led in self.led_range:
                    pixels[led] = self.current_celebration_color
                self.update_celebration_color()
            else:
                # TODO: Jouer l'animation
                for led in self.led_range:
                    pixels[led] = (23, 23, 13, 0)

        return door_leds

    def change_day(self, current_day: datetime, sun_times):
        self.morning_times = get_morning_times(sun_times)
        self.evening_times = get_evening_times(sun_times)
        print(f'Sun times :{sun_times["sunrise"]} -> {sun_times["sunset"]}')
        print(
            f"Door {self.day_number} ({self.led_range}): Morning {self.morning_times[0]} -> {self.morning_times[1]} - "
            f"Evening {self.evening_times[0]} -> {self.evening_times[1]}")
        self.is_door_day = current_day.day == self.day_number

    def update_celebration_color(self):
        if self.current_celebration_color[WHITE_INDEX] == 250:
            self.celebration_decreasing_color = WHITE_INDEX
            self.celebration_increasing_color = RED_INDEX
        elif self.current_celebration_color[WHITE_INDEX] == 0:
            self.celebration_decreasing_color = RED_INDEX
            self.celebration_increasing_color = WHITE_INDEX
        self.current_celebration_color[self.celebration_decreasing_color] -= 1
        self.current_celebration_color[self.celebration_increasing_color] += 1
