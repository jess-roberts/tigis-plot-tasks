Project: TIGIS Assessments
Author: B068747

GENERAL NOTES
--------------
- this project contains two main programs, named 'task_1' and 'task_2' which
 complete the separate tasks required for the assignment
- the package and modules created in this project are only utilised by task_2
- task_1 and task_2 do not link in any form
- the data files required by task_1 and task_2 are contained within the 
project (and thus the programs must not be separated from and moved within
 the project directory)

TASK_1
==========================================================================
- this program contains a function that reads the dataset 'plenty.data'
- the function definition is contained within the program to avoid 
redundantly separating it, as it is not used in task_2

TASK_2
==========================================================================
- this program contains packages which parse the file 'natural_neighbourhoods.dat' 
(sourced from City of Edinburgh Council Mapping Portal, licensed under Open Government 
License v3.0) and plot it through user controls
- the file parser package separates the data according it its type, and 
 stores the data in a dictionary
- the plotting package contain two modules, one which piggybacks the user
 control and runs slightly different plot functions dependent if the user
wants 'all' the data, or just one area

Map Output Notes
-----------------
- the plotting package uses 'edin_SAVI_277.tif' as a background image basemap 
(sourced from https://eos.com/landviewer/)
- 'SAVI' (soil adjusted vegetation index) satellite imagery was chosen solely for
visualisation due to its clear distinction between water and land 
- map is deliberately not re-scaled for individual areas selected for the
purpose of generating an overview
    
