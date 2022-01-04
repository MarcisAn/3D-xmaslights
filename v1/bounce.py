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



# Define functions which animate LEDs in various ways.

# Main program logic follows:
#x = [0, 5, 2, 6, 1, 7, 4, 3, 9, 8, 11, 12, 14, 10, 15, 16, 13, 151, 60, 163, 58, 79, 153, 174, 78, 149, 175, 61, 91, 88, 83, 86, 89, 90, 178, 92, 98, 160, 176, 82, 81, 94, 57, 59, 147, 161, 99, 145, 100, 164, 158, 156, 38, 106, 162, 104, 62, 80, 53, 54, 159, 37, 41, 39, 101, 157, 19, 20, 154, 150, 76, 152, 105, 121, 96, 165, 63, 144, 143, 17, 77, 97, 93, 64, 18, 148, 146, 173, 56, 166, 95, 113, 177, 172, 107, 73, 179, 122, 117, 21, 75, 103, 128, 84, 40, 87, 123, 102, 181, 52, 50, 55, 180, 35, 85, 36, 186, 187, 184, 45, 198, 169, 195, 155, 43, 194, 193, 42, 74, 126, 125, 199, 108, 120, 69, 109, 167, 51, 190, 168, 185, 171, 72, 44, 67, 23, 170, 33, 22, 65, 110, 188, 196, 142, 127, 119, 183, 70, 49, 139, 66, 71, 189, 34, 114, 112, 182, 118, 141, 129, 130, 140, 133, 116, 24, 124, 46, 68, 47, 197, 30, 25, 131, 115, 132, 191, 137, 111, 192, 134, 135, 136, 31, 26, 32, 48, 138, 27, 29, 28]


if __name__ == '__main__':
    x = [0, 1, 2, 3, 40, 4, 41, 11, 10, 42, 39, 43, 48, 12, 17, 5, 15, 44, 18, 49, 8, 9, 27, 28, 47, 32, 6, 38, 7, 19, 16, 33, 30, 46, 37, 26, 60, 45, 20, 58, 35, 14, 31, 61, 21, 13, 64, 105, 25, 78, 62, 29, 56, 59, 50, 93, 106, 34, 76, 79, 55, 75, 77, 36, 94, 107, 118, 103, 73, 90, 102, 57, 24, 67, 104, 89, 92, 121, 54, 51, 120, 101, 80, 122, 108, 117, 71, 65, 66, 22, 23, 91, 119, 63, 116, 74, 72, 53, 123, 96, 52, 81, 69, 68, 95, 97, 88, 82, 124, 100, 70, 109, 114, 113, 115, 98, 87, 86, 83, 112, 110, 125, 137, 85, 99, 111, 139, 84, 154, 136, 138, 153, 155, 126, 140, 141, 156, 127, 160, 161, 146, 159, 142, 163, 147, 151, 135, 152, 162, 167, 133, 157, 134, 129, 144, 158, 149, 128, 148, 168, 166, 143, 169, 145, 165, 132, 164, 130, 150, 186, 131, 183, 170, 185, 182, 179, 189, 181, 171, 188, 184, 180, 190, 178, 191, 172, 187, 177, 175, 176, 174, 192, 173, 193, 195, 194, 196, 199, 197, 198]
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    strip.setPixelColor(2, Color(0,0,255))
    i = 0
    j=0
    
    try:
         while True:
             i=0
             t = 0
             while t < 180:
                 strip.setPixelColor(x[t], Color(0,0,255))
                 strip.setPixelColor(x[t-20], Color(0,0,0))
                 strip.show()
                 t = t+1
             t = 199
             while t > 20:
                 strip.setPixelColor(x[t], Color(0,255,0))
                 try:
                     strip.setPixelColor(x[t+20], Color(0,0,255))
                 except:
                     pass
                 strip.show()
                 t = t-1
             
         list_a = []
         a = 0
         while(a<200):
            list_a.append(a)
            a = a+1
   #      print(list_a)
    #     while(i<200):
     #        print(i)
      #       strip.setPixelColor(i, Color(0,0,0))
       #      i = i+1
        # strip.show()
         print(quick_sort(list_a))
        
    except KeyboardInterrupt:
        i = 0
        while(i<200):
            strip.setPixelColor(i, 0)
            i = i+1


