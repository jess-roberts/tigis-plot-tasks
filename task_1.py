#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: B068747
"""

from matplotlib import pyplot as plt

"""
    Function to parse a continuous dataset
"""

def simple_parse(filename):
    # setting up empty x and y co-ordinate lists
    x = []
    y = []
    # opening the data file
    data = open(filename,'r') 
    for line in data.readlines():
        values = [float(values) for values in line.split(' ')] # converting to floats
        x.append(values[0]) # taking the first value as x value
        y.append(values[1:]) # taking infinite values thereafter as y value
    data.close() # closing the data file after value extraction
    return x, y

"""
    Function to create a simple plot
"""

def simple_plot(x, y):
    # plotting the data with example formatting
    plt.plot(x,y,ms=1)
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')
    plt.title('Some Random Title')
    plt.show() 
    return(simple_plot)

"""
    Using these functions on 'plenty.data'
"""

# setting the data to plot
fname = 'plenty.data'

# parsing and plotting selected data
x, y = simple_parse(fname)
simple_plot(x, y)