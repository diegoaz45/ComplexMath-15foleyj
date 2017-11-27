#!/usr/bin/python
# made by ComplexMath-15foleyj

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()
import time

PARA = 1
SERI = 0
POLAR = 1
RECT = 0

lcd.message("Series?\n")
time.sleep(1)
lcd.message("<- Yes No ->")
while (True):
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        lcd.message("Series Selected")
        circuit = SERI
        time.sleep(3)
        lcd.clear()
        break

    elif (lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        lcd.message("Parallel Selected")
        circuit = PARA
        time.sleep(3)
        lcd.clear()
        break

lcd.message("Polar?\n")
time.sleep(1)
lcd.message("<- Yes No ->")
while (True):
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        lcd.message("Polar Selected")
        numtype = POLAR
        time.sleep(3)
        lcd.clear()
        break

    elif (lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        lcd.message("Rectangular Selected")
        numtype = RECT
        time.sleep(3)
        lcd.clear()
        break





