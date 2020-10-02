import re
_all__ = ['file_parser']


"""
    Functions to parse a file according to the data contained
    in each line
"""

def setHeader(d, k):
    d[k] = "" # setting up the fill header function 

def parse_file(filename):
    # setting empty arrays and dicts to fill
    dictionary = {}
    comments = []
    current_header = []   
    with open(filename) as f:
        fh = f.read().splitlines() # reading the file into lines
    for line in fh:
        first_char = line[:1] # testing the first character of each line
        if line == '': # moving past the blanks
            continue
        elif first_char == '#': # checking if its a comment
            comments.append(line) # removing comments to another list
        elif re.match('[A-Za-z]', first_char): # testing for letters (header)
            setHeader(dictionary, line) # put line identified as header as header
            current_header = line # put header into list of headers
        else: # if its not a blank, comment or header...
            line = re.findall(r'\d+.\d+', line)  # extract the digits from the line
            line = [float(vals) for vals in line] # float values for plotting
            try: # add the digit data to the current header
                dictionary[current_header].extend(line) # add lines to the right header
            except: # if there's nothing to extend on to 
                dictionary[current_header] = line # start as the first line
        f.close() # close file after extraction
    return dictionary, comments
