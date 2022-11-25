import time

from door import Door
from tools import get_now, get_sun_times

# import board
# import neopixel
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
# ORDER = neopixel.GRB
# PIN = board.D18  # NeoPixels must be connected to D10, D12, D18 or D21 to work.
NUMPIXELS = 90  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
AUTO_WRITE = True  # False: Force call to 'pixels.show()' in order to display color

# pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=AUTO_WRITE, pixel_order=ORDER)

checkin = time.monotonic()
counter = 0
seconds = 0

if __name__ == '__main__':
    current_time = get_now()
    current_day = None
    village = [
        Door(1, range(0, 9)),
        Door(3, range(27, 36)),
        Door(5, range(9, 18)),
        Door(7, range(78, 84)),
        Door(9, range(45, 54)),
        Door(11, range(54, 63)),
        Door(13, range(18, 27)),
        Door(15, range(84, 91)),
        Door(17, range(36, 45)),
        Door(19, range(63, 71)),
        Door(21, range(72, 78)),
    ]

    while True:
        # time.sleep(0.1)  # In sec
        counter += 1
        if time.monotonic() - checkin > 1.0:
            seconds += 1
            print("(approx)", seconds, "seconds have elapsed.", counter, "loops")
            checkin = time.monotonic()
            counter = 0

        if current_time.day != current_day:
            current_day = current_time.day
            sun_times = get_sun_times()
            for door in village:
                door.change_day(current_time, sun_times)

        for door in village:
            door_leds = door.get_door_leds_state(current_time)
            for led_number in door_leds:
                # pixels[led_number] = door_leds[led_number]
                # print(f"{led_number} -> {door_leds[led_number]}")
                pass
