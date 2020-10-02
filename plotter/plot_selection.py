_all__ = ['plot_selection']

"""
    Separate functions for plotting different data from the dictionary 
    based on user inputs within the program
"""

def All(dictionary):
    # set up empty arrays to fill
    x = []
    y = []
    for keys, areas in dictionary.items():
        x.append(areas[0::2]) # take the even indices (x)
        y.append(areas[1::2]) # take the odd indicies (y)
        title = 'Edinburgh\'s Natural Neighbourhoods'
    return x, y, title

def One(dictionary, string1):
    # setting up empty arrays and variables to fill
    x = []
    y = []
    target_vals = ''
    target_vals = dictionary.get(string1) # selecting the data the user asked for
    x.append(target_vals[0::2]) # take the even indices (x)
    y.append(target_vals[1::2])# take the odd indicies (y)
    title = string1
    return x, y, title