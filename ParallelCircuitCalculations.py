#! Parallel Calculations
# Josie Foley
# Computer Electronics @ Vincennes University

import math
from math import pi

#User Input Frequecy
freqValue = input('\nWhat is the frequency? ')
print 'Frequency is: ' , freqValue
#User Input Resistor
resistorValue = input('\nWhat is the value of the resistor? (In Ohms) ')
print 'Resistor Value is: ' , resistorValue

#User Input Capcacitor
capValue = input('\nWhat is the value of the Capacitor? (In Farads) ')
print 'Capacitor Value is: ' , capValue
capOhm = 2*pi*freqValue*capValue
capRes = 1/capOhm
print 'Capacitor Value in ohms is: ' , capRes

#User Input Inductor
indValue = input('\nWhat is the value of the Inductor? (In Henrys) ')
print 'Inductor Value is: ' , indValue
indRes = 2*pi*freqValue*indValue
print 'Inductor Value in ohms is: ' , indRes


#THIS IS STARTING CIRCUIT CALCULATIONS
#PARALLEL BRANCH

print '\nNow we will start parallel calculations'
print 'Taking 1 divided by variables. (Lower half of parallel equation)'
paraRes = 1/float(resistorValue)
print 'Resistor is: ' , paraRes

paraCap = 1/capRes
print 'Capacitor is: ' , paraCap

paraInd = 1/indRes
print 'Inductor is: ' , paraInd

print 'Adding those together: '
combTotal = paraRes+paraCap+paraInd
print 'Total is: ' , combTotal
print 'Next, invert that total to get total parallel resistance'
invCombTotal = 1 /combTotal
print 'Total Parallel Resistance is: ' , invCombTotal








