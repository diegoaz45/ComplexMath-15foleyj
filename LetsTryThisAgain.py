#!/usr/bin/python
# Josie
# Putting together series and parallel
import math
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
import time 

pi = 3.1415926535897932384626433832


# Rectangular to Polar Conversion.
def rect_to_polar(x, y):
    angle = math.atan((y/x))
    angle = angle * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer
# Polar to Rect conversion.
def polar_to_rect(polar_num):
    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))
    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))
    rect = x, y
    return rect
# Magnitude function for later use. Takes a real + j number and returns the magnitude
def magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1] * number[1]))
    return absolute

def complex_add(complex_a,complex_b):

    x1 = float(complex_a[0]) * math.cos(pi/180 * complex_a[1])
    x2 = float(complex_b[0]) * math.cos(pi/180 * complex_b[1])
    y1 = float(complex_a[0]) * math.sin(pi/180 * complex_a[1])
    y2 = float(complex_b[0]) * math.sin(pi/180 * complex_b[1])
    x_total = x1 + x2
    y_total = y1 + y2
    answer = rect_to_polar(x_total, y_total)
    return answer[0], answer[1]

def complex_division(complex_a, complex_b):
    real_answer = complex_a[0] / complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer


def complex_multiplication(complex_a, complex_b):
    real_answer = complex_a[0] * complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer



# **************************************************************************************

# Stating variables
PARA = 1
SERI = 0
POLAR = 1
RECT = 0

# Series or Parallel
lcd.message("Series?\n")
time.sleep(1)
lcd.message("<- Yes No ->")
while(True):
    if (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        lcd.message("Series Selected")
        circuit = SERI
        time.sleep(2)
        lcd.clear()
        break
        
    elif(lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        lcd.message("Parallel Selected")
        circuit = PARA
        time.sleep(2)
        lcd.clear()
        break
# *********************************************************************************************************

# Series Branch Calculations
if (circuit == 0):
    print('Series Circuit')
    print('If a value is not present, please type 0')

    lcd.message("Polar Answers?\n")
    time.sleep(1)
    lcd.message("<- Yes No ->")
    while(True):
        if (lcd.is_pressed(LCD.LEFT)):
            lcd.clear()
            lcd.message("Polar Selected")
            numtype = POLAR
            time.sleep(3)
            lcd.clear()
            break
        
        elif(lcd.is_pressed(LCD.RIGHT)):
            lcd.clear()
            lcd.message("Rectangular Selected")
            numtype = RECT
            time.sleep(3)
            lcd.clear()
            break
    
    frequency = input('\nWhat is the frequency of the source? (in Hz): ')
    voltage = input('\nWhat is the voltage of the source? (in RMS): ')
    resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
    inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
    inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? (in Ohms): ')
    capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')

# Some basic calculations
    omega = 2 * pi * frequency
    total_resistance = inductor_resistance + resistor_value
    inductance = omega * inductor_value
    mag_inductance = (inductor_resistance, inductance)
    mag_inductance = magnitude(mag_inductance)
    capacitance = (1/(omega * capacitor_value))
    impedance = total_resistance, (inductance + -capacitance)
    mag_impedance = magnitude(impedance)
    current = float(voltage) / float(mag_impedance)
    v_r = current * resistor_value
    v_l = current * inductance
    v_c = current * capacitance

# Phase Angle
    if inductance > capacitance:
        argument_send = impedance[1] / impedance[0]
    else:
        if capacitance > inductance:
            argument_send = impedance[0] / impedance[1]
        else:
            argument_send = 0
    phase_radians = math.atan(argument_send)
    phase_angle = phase_radians * 180/pi

# Printing out the results
    if capacitance > inductance:
        print('Current will lead your voltage by %f degrees ' % phase_angle)
    if inductance > capacitance:
        print('Current will lag your voltage by %f degrees' % phase_angle)
    #print('\nTotal impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
    #print('Magnitude of your impedance is: %.2f' % mag_impedance)
    #print('Current is: %f A' % current)
    #print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (v_r, v_l, v_c))

# ***************************************************************************************

# Parallel branch.
if (circuit == 1):
    print('Parallel Circuit')

    lcd.message("Polar Answers?\n")
    time.sleep(1)
    lcd.message("<- Yes No ->")
    while(True):
        if (lcd.is_pressed(LCD.LEFT)):
            lcd.clear()
            lcd.message("Polar Selected")
            numtype = POLAR
            time.sleep(3)
            lcd.clear()
            break
        
        elif(lcd.is_pressed(LCD.RIGHT)):
            lcd.clear()
            lcd.message("Rectangular Selected")
            numtype = RECT
            time.sleep(3)
            lcd.clear()
            break

        
    print('If a value is not present, please type 0')
    frequency = input('\nWhat is the frequency of the source? (in Hz): ')
    voltage = input('\nWhat is the voltage of the source? (in RMS): ')
    resistor_value = input('\nWhat value of resistor is present? (in Ohms): ')
    inductor_value = input('\nWhat is the value of your inductor? (in Henrys): ')
    inductor_resistance = input('\nWhat is the resistance of the wiring of the inductor? (in Ohms): ')
    capacitor_value = input('\nWhat is the value of your capacitor? (in Farads): ')


# Calculations. Polar format.
    polar_voltage = voltage, 0
    omega = 2 * pi * frequency
    resistor_value = float(resistor_value)
    resistance = float(resistor_value), 0
    inductor_resistance = inductor_resistance, 0
    inductance = (omega * inductor_value), 90
    capacitance = 1/(omega*capacitor_value), -90
    inductor_branch = complex_add(inductor_resistance, inductance)
    one = 1, 0

# Inverse of the impedances
    inverse_resistance = complex_division(one, resistance)
    inverse_p_capacitance = complex_division(one, capacitance)
    inverse_p_inductance = complex_division(one, inductor_branch)

# Current formula 1 / ((1/Xl) + (1/R) + (1/Xc))
    denominator = complex_add(inverse_p_capacitance, inverse_p_inductance)
    denominator_f = complex_add(denominator, inverse_resistance)
    total_impedance = complex_division(one, denominator_f)

# Current calculations (Parallel)
    total_current = voltage / total_impedance[0]
    inductor_branch_current = total_current * (total_impedance[0] / inductor_branch[0])
    cap_branch_current = total_current * (total_impedance[0] / capacitance[0])
    resistor_branch_current = total_current * (total_impedance[0] / resistance[0])

# Results
    #print('The magnitude of your impedance is %f with a phase of %f degrees' % (total_impedance[0], total_impedance[1]))
    if total_impedance[1] > 0:
        print('Current will be lagging voltage by %f degrees' % total_impedance[1])
    if total_impedance[1] < 0:
        print('Current will be leading voltage by %f degrees' % total_impedance[1])
    if total_impedance[1] == 0:
        print('Voltage and current will be in phase!')
    #print('Total current will be %f A' % total_current)
