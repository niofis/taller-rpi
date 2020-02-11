# OLED Display
# VCC -> 3.3V (Pin 1)
# GND -> GND (Pin 6)
# SCL -> GPIO 3 (Pin 5)
# SDA -> GPIO 2 (Pin 3)
import time
import sys
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

while True:
    try:
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((0,0), "OLED!",  font=font, fill=1)
        draw.line((0,0, 127, 63), fill=1)
        disp.image(image)
        disp.display()
        time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()
