import numpy as np
import matplotlib.pyplot as plt
import sys

import PySpice
import PySpice.Logging.Logging as Logging
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import * # meaning for example selecting ohm for a resistor


# Functions

def format_output(analysis):
    '''
    Gets dictionary containing SPICE sim values.
    The dictionary is created by pairing each of the nodes to its corresponding
    output voltage value array.
    This provides a more manageble format.
    '''

    sim_res_dict = {} # create dictionary

    # loop though nodes
    for node in analysis.nodes.values():
        data_label = "%s" % str(node) # extract node name
        sim_res_dict[data_label] = np.array(node) # save node value/array of values
    
    # # if the simulation mode is set to 'trans', save time array also
    # if sim_mode == 'trans':
    #     t = []
    #     for val in analysis.time:
    #         t.append(val)
    #     sim_res_dict['time'] = np.array(t)

    return sim_res_dict



# making a simple voltage divider
# run an operating point analysis

# Create the circuit
circuit = Circuit('Voltage Divider')

# Add components to the circuit
circuit.V('input', "In", circuit.gnd, 10@u_V)  # Voltage source
#        (name, connected to one side, connected to second side, voltage)
circuit.R(1, "In", 'out', 9@u_kOhm) # Resistor 1
circuit.R(2, 'out', circuit.gnd, 1@u_kOhm)

# Create a simulator object
simulator = circuit.simulator(temperature = 25, nominal_temperature = 25)

# Print the circuit
# print("The Circuit/Netlist:\n\n", circuit)

# Print the circuit + simulator delatils:
# print("The simulator:\n\n", simulator)

# Run analysis
analysis = simulator.operating_point() #pre formated and data can be extracted in various ways

# print(analysis) 

# print(analysis.nodes['in'])
# print(str(analysis.nodes['in']))
# print(float(analysis.nodes['in']))


# print(str(analysis.nodes['out']))
# print(float(analysis.nodes['out']))

out_dict = format_output(analysis) # do formating

print(out_dict)


