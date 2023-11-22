from flask import Flask, render_template, request, jsonify
import sys

from common.neopixelwrapper import pixels

sys.path.insert(0, '/home/pi/christmass_light')

# from neopixelwrapper import pixels

app = Flask(__name__)

# NUMPIXELS = 90  # Update this to match the number of LEDs.
# BRIGHTNESS = 1  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
# AUTO_WRITE = True  # False: Force call to 'pixels.show()' in order to display color
#
# import board
# import neopixel
#
# PIN = board.D18  # NeoPixels must be connected to D10, D12, D18 or D21 to work.
# pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=AUTO_WRITE,
#                            bpp=4)
#


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_color', methods=['POST'])
def update_color():
    r = request.form['r']
    g = request.form['g']
    b = request.form['b']
    w = request.form['w']
    color = f'#{int(r):02x}{int(g):02x}{int(b):02x}'
    pixels.fill((int(r), int(g), int(b), int(w)))
    pixels.show()
    # pixels.fill((int(r), int(g), int(b)))
    return jsonify(color=color)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
