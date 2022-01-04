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

def quick_sort(sequence):
    print("helo", sequence)
    lenght = len(sequence)
    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_grater = []
    items_lower = []
    
    for item in sequence:
        strip.setPixelColor(item, Color(255,0,0))
        strip.setPixelColor(pivot, Color(0,255,0))
        strip.show()
        i = input("vai zalais ir talak par sarkano j-n")
        if i == "j":
            items_grater.append(item)
        else:
            items_lower.append(item)
        strip.setPixelColor(item, Color(0,0,0))
        strip.setPixelColor(pivot, Color(0,0,0))
        strip.show()
    return quick_sort(items_lower) + [pivot] + quick_sort(items_grater)

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    try:
         list_a = []
         a = 0
         while(a<200):
            list_a.append(a)
            a = a+1
         print(quick_sort(list_a))
        
    except KeyboardInterrupt:
        i = 0
        while(i<200):
            strip.setPixelColor(i, 0)
            i = i+1