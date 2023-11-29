import logging
from datetime import time, datetime, timedelta
from random import randint, choices, choice


from christmas_village.animations import CELEBRATIONS, ANIMATIONS
from common.neopixelwrapper import pixels, WHITE_INDEX, RED_INDEX

CELEBRATION_COLOR_1 = WHITE_INDEX
CELEBRATION_COLOR_2 = RED_INDEX

MORNING_LIGHT_UP_MIN_HOUR = 6
MORNING_LIGHT_UP_MAX_HOUR = 9
EVENING_SHUTDOWN_MIN_HOUR = 21
EVENING_SHUTDOWN_MAX_HOUR = 23


def get_morning_times(sun_time):
    morning_light_up = (sun_time["sunrise"] - timedelta(minutes=randint(15, 120))).time()
    morning_shutdown = (sun_time["sunrise"] + timedelta(minutes=randint(0, 30))).time()
    # morning_light_up = time(randint(MORNING_LIGHT_UP_MIN_HOUR, MORNING_LIGHT_UP_MAX_HOUR), randint(0, 59))
    return [morning_light_up, morning_shutdown]


def get_evening_times(sun_time):
    evening_light_up = (sun_time["sunset"] + timedelta(minutes=randint(-10, 120))).time()
    evening_shutdown = time(randint(EVENING_SHUTDOWN_MIN_HOUR, EVENING_SHUTDOWN_MAX_HOUR), randint(0, 59))
    return [evening_light_up, evening_shutdown]


class Door:
    def __init__(self, day_number: int, led_range: [int]):
        self.day_number = day_number
        self.led_range = led_range
        self.morning_times = None
        self.evening_times = None
        self.is_door_day = False
        self.is_light_up = False

        self.current_animation = None
        self.current_animation_state = []
        self.remaining_time_on_current_animation_state = 0
        self.remaining_time_on_current_animation = 0

        self.current_celebration_color = [0, 0, 0, 0]
        self.celebration_increasing_color = CELEBRATION_COLOR_1
        self.celebration_decreasing_color = CELEBRATION_COLOR_2

    def should_light(self, current_datetime: datetime):
        should_light = (self.evening_times[0] < current_datetime.time() < self.evening_times[1]
                        or self.morning_times[0] < current_datetime.time() < self.morning_times[1]
                        or (self.is_door_day
                            and self.evening_times[1] > current_datetime.time() > self.morning_times[0])
                        )
        if should_light and self.is_light_up:
            return True
        elif should_light and not self.is_light_up:
            logging.debug(f"Door {self.day_number} light-up.")
            self.is_light_up = True
            return True
        elif not should_light and not self.is_light_up:
            return False
        elif not should_light and not self.is_light_up:
            logging.debug(f"Door {self.day_number} shutdown.")
            self.is_light_up = False
            return False

    def update_door_leds_state(self, current_datetime: datetime):
        # TODO : Calculer le "should change" en utilisant un timer pour éviter des changements de clock
        if self.should_light(current_datetime):
            # deprecated, use celebration now
            # if self.is_door_day:
                # self.light(self.current_celebration_color)
                # self.update_celebration_color()
                # self.play_animation()
            # else:
            self.play_animation()
        else:
            self.shutdown()

    def light(self, color):
        for led in self.led_range:
            pixels[led] = color

    def shutdown(self):
        for led in self.led_range:
            pixels[led] = (0, 0, 0, 0)

    def change_day(self, current_day: datetime, sun_times):
        self.morning_times = get_morning_times(sun_times)
        self.evening_times = get_evening_times(sun_times)
        logging.info(
            f"Door {self.day_number} ({self.led_range}): Morning {self.morning_times[0]} -> {self.morning_times[1]} - "
            f"Evening {self.evening_times[0]} -> {self.evening_times[1]}")
        self.is_door_day = current_day.day == self.day_number

    # @deprecated
    def update_celebration_color(self):
        if self.current_celebration_color[CELEBRATION_COLOR_2] == 250:
            self.celebration_decreasing_color = CELEBRATION_COLOR_2
            self.celebration_increasing_color = CELEBRATION_COLOR_1
        elif self.current_celebration_color[CELEBRATION_COLOR_1] == 250:
            self.celebration_decreasing_color = CELEBRATION_COLOR_1
            self.celebration_increasing_color = CELEBRATION_COLOR_2
        elif (self.current_celebration_color[CELEBRATION_COLOR_2] == 0 and
              self.current_celebration_color[CELEBRATION_COLOR_1] == 0):
            self.current_celebration_color[CELEBRATION_COLOR_1] = 0
            self.current_celebration_color[CELEBRATION_COLOR_2] = 250
            return

        self.current_celebration_color[self.celebration_decreasing_color] -= 1
        self.current_celebration_color[self.celebration_increasing_color] += 1

    def choose_animation(self):
        animations_list = CELEBRATIONS if self.is_door_day else ANIMATIONS

        animations = [sublist[0] for sublist in animations_list]
        animations_weight = [sublist[1] for sublist in animations_list]

        self.current_animation = choices(animations, weights=animations_weight, k=1)[0]
        self.remaining_time_on_current_animation = randint(int(self.current_animation["max_duration"] / 2),
                                                           self.current_animation["max_duration"])
        logging.debug(f"Animation door {self.day_number}: {self.current_animation['name']}")

    def play_animation(self):
        if self.remaining_time_on_current_animation == 0:
            self.choose_animation()
            logging.debug(f"Door {self.day_number} new animation: {self.current_animation['name']}")
        else:
            self.remaining_time_on_current_animation -= 1
            if self.remaining_time_on_current_animation_state > 0:
                self.remaining_time_on_current_animation_state -= 1
            else:
                self.generate_new_animation_state()

            self.display_animation()

    def generate_new_animation_state(self):
        colors = [sublist[0] for sublist in self.current_animation["weighted_colors"]]
        self.remaining_time_on_current_animation_state = randint(1, self.current_animation["max_speed"])
        if not self.current_animation["full_blink"]:
            colors_weight = [sublist[1] for sublist in self.current_animation["weighted_colors"]]
            self.current_animation_state = choices(colors, weights=colors_weight, k=len(self.led_range))
        else:
            self.current_animation_state = [choice(colors)] * len(self.led_range)

    def display_animation(self):
        for index, led in enumerate(self.led_range):
            pixels[led] = self.current_animation_state[index]
