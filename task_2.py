#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: B068747
"""

"""
    STAGE ONE: set-up
    importing customised packages and modules
"""

import parser
import plotter
import sys

"""
    STAGE TWO: data input
    loading file and storing its data in a dictionary
    in addition to comments, which are important for reference
"""

fname = 'natural_neighbourhoods.dat'
dictionary, comments = parser.parse_file(fname)

"""
    STAGE THREE: plotting
    giving the user control on what to plot
"""

string1 = input("What area would you like to view? If you'd like to view them all, simply type \'all\': ")

checkpoint = ''

if string1 == "all":
    x, y, title = plotter.All(dictionary) # calling function to loop through data
    checkpoint = 0 # a signal for later plotting
elif string1 in dictionary:
    try:
        x, y, title = plotter.One(dictionary, string1) # calling function to take only one key
        checkpoint = 0 # a signal for later plotting
    except ValueError: # if the user enters an invalid answer
        print('Sorry, that was not a valid choice.')
        checkpoint = 1 # making sure it doesn't produce an empty plot

if checkpoint == 0: # making sure we have data to plot assigned from before
    plotter.map_plotter(x, y) # plotting the areas in a loop, on to a cartopy grid
    plotter.map_format(title) # general formatting 
else:
    print('Sorry, that was not a valid choice.')
    sys.exit()

