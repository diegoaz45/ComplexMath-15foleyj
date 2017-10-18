#! Josie Foley
# Vincennes University Electronics Department
# ComplexMath Series Circuit
# Rev 2 adds polar to rectangular conversions and vice versa.
# Includes basic series circuit calculations.

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






