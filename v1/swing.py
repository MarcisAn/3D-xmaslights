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
    x = [0, 2, 4, 5, 6, 7, 8, 1, 3, 11, 10, 9, 12, 13, 15, 14, 16, 22, 23, 25, 24, 26, 32, 21, 18, 31, 28, 17, 29, 27, 30, 19, 35, 33, 20, 36, 37, 38, 39, 43, 45, 40, 44, 48, 34, 47, 41, 42, 49, 75, 46, 73, 74, 80, 82, 76, 79, 77, 67, 66, 64, 72, 70, 68, 81, 63, 69, 83, 51, 50, 78, 71, 84, 53, 54, 52, 65, 62, 85, 61, 55, 56, 60, 86, 91, 59, 57, 92, 93, 88, 87, 58, 94, 89, 103, 104, 105, 106, 90, 108, 102, 111, 110, 125, 112, 100, 101, 107, 126, 95, 123, 124, 96, 128, 113, 109, 131, 114, 132, 130, 129, 97, 127, 115, 140, 121, 141, 142, 122, 139, 118, 116, 119, 143, 133, 99, 144, 120, 134, 148, 146, 135, 136, 147, 117, 149, 138, 98, 137, 150, 151, 145, 174, 152, 153, 175, 176, 177, 172, 155, 178, 173, 182, 170, 154, 157, 183, 171, 159, 169, 180, 162, 164, 158, 181, 156, 160, 185, 166, 163, 161, 184, 179, 186, 168, 187, 165, 167, 188, 190, 189, 191, 192, 199, 194, 193, 198, 195, 197, 196]
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
             i=199
             t = 0
             while t < 199:
                 strip.setPixelColor(x[-t], Color(255,0,0))                
                 strip.show()
                 time.sleep(0.02)
                 t = t+1
             
             while i > 0:
                 strip.setPixelColor(x[i], Color(0,0,0))
                 strip.show()
                 i -= 1 
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


