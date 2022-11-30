import board
import neopixel

PIN = board.D18  # NeoPixels must be connected to D10, D12, D18 or D21 to work.

pixels = neopixel.NeoPixel(PIN, 90, brightness=1, auto_write=True, bpp=4)

#pixels.fill((0,0,0,255))
while True:
    for led in range(0,90):
        pixels[led] = (0,0,255,0)
        #time.sleep(0.3)
        #print("led N°:" + str(led))
        pixels.fill((0,0,0))