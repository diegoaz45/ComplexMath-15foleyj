#! Josie Foley
# Vincennes University Electronics Department
# ComplexMath Series Circuit
# Rev 2 adds polar to rectangular conversions and vice versa.
# Includes basic series circuit calculations.


def complex_add(complex_a, complex_b):
    real_answer = complex_a[0] + complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in magnitude, phase. Returns the difference of B from A

def complex_subtract(complex_a, complex_b):
    real_answer = complex_a[0] - complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in magnitude, phase. Returns the quotient of B from A

def complex_division(complex_a, complex_b):
    real_answer = complex_a[0] / complex_b[0]
    imag_answer = complex_a[1] - complex_b[1]
    return real_answer, imag_answer


# Expects complex numbers in magnitude, phase. Returns the product of A and B

def complex_multiplication(complex_a, complex_b):
    real_answer = complex_a[0] * complex_b[0]
    imag_answer = complex_a[1] + complex_b[1]
    return real_answer, imag_answer


# Rectangular to Polar. Returns in (r, theta)

def rect_to_polar(x, y):
    angle = math.atan((y/x))
    angle = angle * (180/pi)
    magnitude = (math.sqrt((x*x)+(y*y)))
    answer = magnitude, angle
    return answer

# Polar to Rectangular. Returns the X & Y lengths.

def polar_to_rect(polar_num):
    y = polar_num[0] * (math.sin(polar_num[1] * pi/180))
    x = polar_num[0] * (math.cos(polar_num[1] * pi/180))
    rect = x, y
    return rect

# Magnitude function 
def magnitude(number):
    absolute = math.sqrt((number[0] * number[0]) + (number[1]* number[1]))
    return absolute

import math
from math import pi 
#Recieve all information from user. 
print('Today we will be conducting series AC calculations with R, L, and C.')
frequency = input('\nWhat is the frequency we are working with?: ')
voltage = input('\nWhat is the value of the source? (In RMS): ')
resistor_value1 = input('\nWhat is the value of the resistor?(Ohms): ')
inductor_value1 = input('\nWhat is the value of the inductor?(Henrys): ')
capacitor_value1 = input('\nWhat is the value of the capacitor?(Farads): ')

#To Find Omega
print('Now we will be doing a few calculations')
print('To find omega, you take 2 * pi * frequency')
print('2*',+pi,'*',+frequency)
omega = 2*pi*frequency
print('Omega is', +omega)


#To Find Inductance
print('To find inductance, omega and the inductor value are multiplied together.')
print(omega,'*',inductor_value1)
inductance = omega*inductor_value1
print('Inductance is', +inductance)


#To Find Capacitance
print('To find capacitance, you need the inversion of omega times the capacitor value.')
print('1/(', omega,'*',capacitor_value1)
capacitance = (1/(omega*inductor_value1))
print('Capacitance is', +capacitance)


#To Find Impedance
impedance = resistor_value1, (inductance + -capacitance)
mag_impedance = magnitude(impedance)
current = float(voltage) / float(mag_impedance)
vr = current * resistor_value1
vl = current * inductance
vc = current * capacitance
print('\nYour total impedance is: %.2f + %.2fj' % (impedance[0], impedance[1]))
print('That means the magnitude of your impedance is: %.2f' % mag_impedance)
print('Which then means your current is: %f A' % current)
print('V(R) = %.2f, V(L) = %.2f, V(C) = %.2f' % (vr, vl, vc))







