import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import * # meaning for example selecting ohm for a resistor

V = 10@u_V
R1 = 1@u_kOhm
R2 = 2@u_kOhm
R3 = 3@u_kOhm

# # making a delta network circuit
# # run an operating point analysis

# Create the circuit
circuit = Circuit('Delta Network Circuit')

# Add components to the circuit
circuit.V('input', 'B', circuit.gnd, V)  # Voltage source
circuit.R(1, 'B', circuit.gnd, R1) # Resistor 1
circuit.R(2, 'B', 'C', R2) # Resistor 2
circuit.R(3, 'C', circuit.gnd, R3) # Resistor 3

# Create a simulator object
simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

# Print the circuit
print("The Circuit/Netlist:\n\n", circuit)

# Run analysis
analysis = simulator.operating_point()

print("Current in BC dependence on R3 (AC points):")
print(float(analysis.nodes['c']))

'''
 We are looking for i2 / R3 which is i3 / R3 = v3
 v3 = v * R3 / (R2 + R3)
 which in out case v3 = 10 * 3 / (2 + 3) = 6 volts
'''

