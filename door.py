import random
from datetime import time, datetime


# FancyLED: For color correction

class Door:
    def __init__(self, day_number: int, led_range: [int]):
        self.day_number = day_number
        self.led_range = led_range
        self.morning_times = None
        self.evening_times = None

    def get_door_leds_state(self, current_time: datetime):
        door_leds = {}
        if self.get_state(current_time):
            for led in self.led_range:
                # Todo allumer détection du son, jouer l'animation
                door_leds[led] = [23, 23, 13]
        return door_leds

    def change_day(self, current_day, sun_time):
        self.morning_times = self.get_morning_times(sun_time)
        self.evening_times = self.get_evening_times(sun_time)
        if current_day == self.day_number:
            # TODO faire une célébration
            pass
        else:
            # Todo calculer choix de l'animation aléatoirement
            pass

    def get_state(self, current_time: datetime):
        if self.evening_times[0] < current_time.time() < self.evening_times[1]:
            return True
        elif self.morning_times[0] < current_time.time() < self.morning_times[1]:
            return False

    def get_morning_times(self, sun_time):
        morning_light_up = time(random.randint(6, 7), random.randint(0, 59))
        morning_shutdown = time(random.randint(7, sun_time["sunrise"].hour + 1), random.randint(0, 59))
        return [morning_light_up, morning_shutdown]

    def get_evening_times(self, sun_time):
        evening_light_up = time(random.randint(sun_time["sunset"].hour - 1, 19), random.randint(0, 59))
        evening_shutdown = time(random.randint(21, 23), random.randint(0, 59))
        return [evening_light_up, evening_shutdown]
