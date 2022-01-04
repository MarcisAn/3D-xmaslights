import json
import time
from rpi_ws281x import *
import argparse
import random

# LED strip configuration:
LED_COUNT      = 200      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    try:
         while True:
             f = open("./lightdata.json")
             lightdata = f.read()
             lightdata = lightdata.split("\n")
             for light in lightdata:
                 try:
                    light = light.split(":")
                    #print(light)
                    index = int(light[0])
                    color = light[1].split(",")
                    strip.setPixelColor(index, Color(int(color[1]), int(color[0]), int(color[2])))
                 except:
                     pass
             strip.show() 


    except KeyboardInterrupt:
        i = 0
        while(i<200):
            strip.setPixelColor(i, 0)
            i = i+1

f = open("./lightdata.json")
data = json.load(f)
print(data)
