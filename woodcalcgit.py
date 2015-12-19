from measurement.measures import Distance

"""Takes input from user and calculates materials for building garden beds
of a particular demension. User inputs demensions, width length and height
of garden bed in feet, as well as the number of beds to be built. All
outputs are in feet. Outputs include the total number feet needed of 2 by
six lumber to build the beds, and calculates the most effecient use of the
lumber by iterating through a list of standard board lengths."""

# calculates total amount of wood per bed
def amount_wood(length, width, height):
	total = 0
	length = length * 2
	width = width * 2
	feet = length + width
	if height == 6 or height == .5:
		total = feet
	elif height == 1:
		total = feet * 2
	elif height == 1.5:
		total = feet * 3
	elif height == 2:
		total = feet * 4
	elif height > 2:
		return 'no calculation for height over two'
	else:
		return 'need specific height in'
	return total

#calculate amount of wood for all beds
def times_beds(num_beds):
	return feet * num_beds

# determine total amount of side peices needed. Same for long and short
def amt_sides(height):
	sides = 0
 	if height == 6 or height == .5:
		height = 1 
	elif height == 1:
		height = 2 
	elif height == 1.5:
		height = 3 
	elif height == 2:
		height =  4
	else:
		return 'need specific height in'
	sides += height * 2 * num_beds
	return sides


# determine most effecient use of materials with least amount of cuts
def board_size(sides, length, width, board_lengths):
	new_boardlist = []
	long_sides = sides
	wide_sides = sides
	while long_sides > 0:  
		for size in board_lengths:
			if size >= length and size % length  >= 0:
				new_boardlist.append(size)
				long_sides -= 1
				break
	while wide_sides > 0:	
		for size in board_lengths:
			if size >= width and size % width >= 0:
				new_boardlist.append(size)
				wide_sides -= 1
				break
					
	return new_boardlist
	

width = float(raw_input('enter width '))

length = float(raw_input('enter length '))

height = float(raw_input('enter height '))

feet = amount_wood(length, width, height)

num_beds = float(raw_input('how many beds of size?'))

sides = amt_sides(height)

board_lengths =  [8, 12, 16, 20, 24]

print feet

print times_beds(num_beds)

print ('you need ' + str(sides) +', '+ str(length) +
 ' foot boards, and ' + str(sides) +', '+ str(width)
+ ' foot boards.')

print board_size(sides, length, width, board_lengths)
