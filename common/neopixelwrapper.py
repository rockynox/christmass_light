import os


class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


# class NeoPixel(Singleton):
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
NUMPIXELS = 90  # Update this to match the number of LEDs.
BRIGHTNESS = 0.5  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
AUTO_WRITE = False  # False: Force call to 'pixels.show()' in order to display color
RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2
WHITE_INDEX = 3
pixels = None

if os.uname().nodename == "lalapi":
    import board
    import neopixel

    PIN = board.D18  # NeoPixels must be connected to D10, D12, D18 or D21 to work.
    pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=AUTO_WRITE,
                               bpp=4)
else:
    from common.mock_pixels import MockPixels

    pixels = MockPixels()
