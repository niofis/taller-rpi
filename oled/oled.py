# OLED Display
# VCC -> 3.3V (Pin 1)
# GND -> GND (Pin 6)
# SCL -> GPIO 3 (Pin 5)
# SDA -> GPIO 2 (Pin 3)mport sys
import time
import board
import adafruit_ssd1306
import busio

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_ssd1306.SSD1306_I2C(128,64,i2c)


dir(display)
while True:
    try:
        display.fill(0)
        display.text("OLED!", 0, 0, 1)
        display.line(0,0,127,63, 1)
        display.show()
        time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()
