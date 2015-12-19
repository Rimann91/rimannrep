Repository for woodcalcgit.py
A Python Program for calculating materials for building raised garden beds

Takes input from user and calculates materials for building garden beds
of a particular demension. User inputs demensions, width length and height
of garden bed in feet, as well as the number of beds to be built. All
outputs are in feet. Outputs include the total number feet needed of 2x6
lumber to build the beds, and calculates the most effecient use of the
lumber by iterating through a list of standard board lengths."

Future plan to create GUI so that this program can be easily used by employees.
------------------------------------------------------------------------------------------------------------------

Functions:

amount_wood - calculates total amount of wood per bed

times_beds - multiplies total amount of wood per bed by amount of beds

amt_sides - determines total amount of side peices needed

board_size - determines most effecient use of materials with least amount of cuts by iterating through a list of 
             standard board lengths. [8,12,16,20,24]. return may need cleaned up. Now prints desired output instead of list.
