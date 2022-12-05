import random
from datetime import time, datetime

from neopixelwrapper import pixels, WHITE_INDEX, RED_INDEX

MAX_ANIMATION_SPEED = 500
ANIMATION_COLORS = [
    [(0, 0, 0, 0), 10],  # Black
    [(200, 80, 00, 0), 50],  # Yellow
    [(0, 0, 70, 200), 1],  # White
    [(200, 30, 0, 0), 40],  # Red
    [(170, 10, 0, 0), 20],  # Red warm
    [(255, 215, 0, 0), 20],  # Gold
]
# TODO: Utiliser les couleurs de fancyLED
# TODO: Faire un object avec des animations

CELEBRATION_COLOR_1 = WHITE_INDEX
CELEBRATION_COLOR_2 = RED_INDEX

MORNING_LIGHT_UP_MIN_HOUR = 6
MORNING_LIGHT_UP_MAX_HOUR = 7
EVENING_SHUTDOWN_MIN_HOUR = 22
EVENING_SHUTDOWN_MAX_HOUR = 23


def get_morning_times(sun_time):
    morning_light_up = time(random.randint(MORNING_LIGHT_UP_MIN_HOUR, MORNING_LIGHT_UP_MAX_HOUR), random.randint(0, 59))
    morning_shutdown = time(random.randint(sun_time["sunrise"].hour, sun_time["sunrise"].hour + 1),
                            random.randint(0, 59))
    return [morning_light_up, morning_shutdown]


def get_evening_times(sun_time):
    evening_light_up = time(random.randint(sun_time["sunset"].hour - 1, sun_time["sunset"].hour + 1),
                            random.randint(0, 59))
    evening_shutdown = time(random.randint(EVENING_SHUTDOWN_MIN_HOUR, EVENING_SHUTDOWN_MAX_HOUR), random.randint(0, 59))
    return [evening_light_up, evening_shutdown]


def generate_animation_state(led_number, animation_colors):
    colors = [sublist[0] for sublist in animation_colors]
    colors_weight = [sublist[1] for sublist in animation_colors]
    return random.choices(colors, weights=colors_weight, k=led_number)


class Door:
    def __init__(self, day_number: int, led_range: [int]):
        self.remaining_time_on_current_animation_state = 0
        self.current_animation_state = []
        self.day_number = day_number
        self.led_range = led_range
        self.morning_times = None
        self.evening_times = None
        self.is_door_day = False

        self.current_celebration_color = [0, 0, 0, 0]
        self.celebration_increasing_color = CELEBRATION_COLOR_1
        self.celebration_decreasing_color = CELEBRATION_COLOR_2

    def should_light(self, current_datetime: datetime):
        return (self.evening_times[0] < current_datetime.time() < self.evening_times[1]
                or self.morning_times[0] < current_datetime.time() < self.morning_times[1]
                or self.is_door_day)

    def update_door_leds_state(self, current_datetime: datetime):
        door_leds = {}
        # TODO: Calculer le "should change" en utilisant un timer pour éviter des changement calculer sur la clock
        if self.should_light(current_datetime):
            if self.is_door_day:
                for led in self.led_range:
                    pixels[led] = self.current_celebration_color
                self.update_celebration_color()
            else:
                self.play_animation(MAX_ANIMATION_SPEED, ANIMATION_COLORS)

        return door_leds

    def light(self, color):
        for led in self.led_range:
            pixels[led] = color

    def shutdown(self):
        for led in self.led_range:
            pixels[led] = (0, 0, 0, 0)

    def change_day(self, current_day: datetime, sun_times):
        self.morning_times = get_morning_times(sun_times)
        self.evening_times = get_evening_times(sun_times)
        print(
            f"Door {self.day_number} ({self.led_range}): Morning {self.morning_times[0]} -> {self.morning_times[1]} - "
            f"Evening {self.evening_times[0]} -> {self.evening_times[1]}")
        self.is_door_day = current_day.day == self.day_number

    def update_celebration_color(self):
        if self.current_celebration_color[CELEBRATION_COLOR_2] == 250:
            self.celebration_decreasing_color = CELEBRATION_COLOR_2
            self.celebration_increasing_color = CELEBRATION_COLOR_1
        elif self.current_celebration_color[CELEBRATION_COLOR_1] == 250:
            self.celebration_decreasing_color = CELEBRATION_COLOR_1
            self.celebration_increasing_color = CELEBRATION_COLOR_2
        elif self.current_celebration_color[CELEBRATION_COLOR_2] == 0 and self.current_celebration_color[
            CELEBRATION_COLOR_1] == 0:
            self.current_celebration_color[CELEBRATION_COLOR_1] = 0
            self.current_celebration_color[CELEBRATION_COLOR_2] = 250
            return

        self.current_celebration_color[self.celebration_decreasing_color] -= 1
        self.current_celebration_color[self.celebration_increasing_color] += 1

    def play_animation(self, max_animation_speed, animation_colors):
        if self.remaining_time_on_current_animation_state > 0:
            self.remaining_time_on_current_animation_state -= 1
        else:
            self.current_animation_state = generate_animation_state(len(self.led_range), animation_colors)
            self.remaining_time_on_current_animation_state = random.randint(1, max_animation_speed)

        for index, led in enumerate(self.led_range):
            pixels[led] = self.current_animation_state[index]
