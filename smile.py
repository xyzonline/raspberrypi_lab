#!/usr/bin/env python
# encoding: utf-8
import time

#from PIL import Image
#from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8


# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through each pixel individually and turn it on.

# Run through each pixel individually and turn it on.
def draw_smile():
        # Clear the display buffer.
        display.clear()
        # Set pixel at position i, j to on.  To turn off a pixel set
        # the last parameter to 0.
        for i in range(2,6):
            display.set_pixel(1, i, 1)
            display.set_pixel(0, i, 1)
        for i in range(3,7):
            display.set_pixel(i, 0, 1)
            display.set_pixel(i, 7, 1)
        display.set_pixel(2, 1, 1)
        display.set_pixel(2, 6, 1)
        display.set_pixel(7, 6, 1)
        display.set_pixel(7, 1, 1)

        # eye
        display.set_pixel(3, 2, 1)
        display.set_pixel(3, 5, 1)
        # mouth
        display.set_pixel(5, 5, 1)
        display.set_pixel(5, 2, 1)
        display.set_pixel(6, 4, 1)
        display.set_pixel(6, 3, 1)
        # Write the display buffer to the hardware.  This must be called to
        # update the actual display LEDs.
        display.write_display()



def draw_sad():
        # Clear the display buffer.
        display.clear()
        # Set pixel at position i, j to on.  To turn off a pixel set
        # the last parameter to 0.
        for i in range(2,6):
            display.set_pixel(1, i, 1)
            display.set_pixel(0, i, 1)
        for i in range(3,7):
            display.set_pixel(i, 0, 1)
            display.set_pixel(i, 7, 1)
        display.set_pixel(2, 1, 1)
        display.set_pixel(2, 6, 1)
        display.set_pixel(7, 6, 1)
        display.set_pixel(7, 1, 1)

        # eye
        display.set_pixel(3, 2, 1)
        display.set_pixel(3, 5, 1)
        # mouth
        display.set_pixel(6, 5, 1)
        display.set_pixel(5, 4, 1)
        display.set_pixel(5, 3, 1)
        display.set_pixel(6, 2, 1)
        # Write the display buffer to the hardware.  This must be called to
        # update the actual display LEDs.
        display.write_display()



# Draw some shapes using the Python Imaging Library.
def clear():
#    draw_smile()
    display.clear()
    display.write_display()
clear()