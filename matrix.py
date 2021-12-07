from machine import Pin, SPI, PWM
import random
import time

import driver

BLACK = 0x0000
GREEN1 = 0x001f
GREEN2 = 0x001c
GREEN3 = 0x001a
WHITE = 0xffff

FONT = 11

lcd = driver.LCD_1inch14()

# Set brightness
pwm = PWM(Pin(driver.BL))
pwm.freq(1000)
pwm.duty_u16(32768)

width = 30
height = 12
size = width*height

chars = [random.choice("0123456789abcdef") for _ in range(size+2*width)]
field = [0 for _ in range(size+2*width)]

while True:
    lcd.fill(BLACK)

    for _ in range(width//30):
        field[int(random.random()*width)] = 15
    for i in range(size+width*2-1, width-1, -1):
        if field[i-width] == 15:
            field[i] = 15
        if field[i-width] > 0:
            field[i-width] -= 1
    for i in range(size):
        attr = BLACK
        if field[i+width] > 14:
            attr = WHITE
        elif field[i+width] > 9:
            attr = GREEN1
        elif field[i+width] > 4:
            attr = GREEN2
        elif field[i+width] > 1:
            attr = GREEN3
        lcd.text(chars[i+width],  FONT * (i % width), FONT * (i//width), attr)
    lcd.show()
    time.sleep(.03)
