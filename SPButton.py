#!/usr/bin/python
#Play with the buttons
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
import time
PARA = 1
SERI = 0

lcd.message("Series?\n")
time.sleep(1)
lcd.message("<- Yes No ->")
while(True):
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        lcd.message("Series Selected")
        circuit = SERI
        time.sleep(5)
        lcd.clear()
        
    elif(lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        lcd.message("Parallel Selected")
        circuit = PARA
        time.sleep(5)
        lcd.clear()


lcd.message("Is this circuit Series (Left Button) or Parallel (Right Button)?")
time.sleep(5)

while(True):
    lcd.clear()
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.message("Series")
        time.sleep(1)

    elif (lcd.is_pressed(LCD.RIGHT)):
        lcd.message("Parallel")
        time.sleep(1)



        
