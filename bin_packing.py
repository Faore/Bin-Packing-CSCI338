# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Chris Thomas, Miriam Rognlie
# Last Modified: February 15, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------

"""
We check our new box against the shortest row. If it
increases the size of the total width less than it
increases the size of the total height we place it in
the shortest row. Otherwise we start a new row.
"""

def find_solution (rectangles):
    map = []
    i = 0
    # Take the rectangles and put them in a hash map,
    # giving them an ID to sort them back when we return the placements.
    for rectangle in rectangles:
        map.append({'id': i, 'rect': rectangle})
        i = i+1
    map.sort(key=lambda dict: dict['rect'][1]) # Sort by height
    map.reverse()
    # Initialize some variables
    placement = []
    rows = []
    totalHeight = 0
    #No rows to begin with, so have something invalid to check against.
    shortestRow = -1
    longestRow = -1
    # There is no width to begin with
    totalWidth = 0

    # Go through all the rectangles (preordered by height)
    for dictionary in map:
        width = dictionary['rect'][0]
        height = dictionary['rect'][1]
        # Find the shortest row.
        if shortestRow != -1:
            for i in range(0, len(rows)):
                if(rows[i][0] < rows[shortestRow][0]):
                    shortestRow = i
        #Check if the total width will be less than the total height if we place on the shortest row.
        if shortestRow != -1 and (rows[shortestRow][0] + width < totalHeight + height):
            #Add to shortest row
            row = shortestRow
            coordinate = rows[shortestRow]
        else:
            #Add to a new row.
            row = len(rows)
            coordinate = (0, totalHeight)

        #Book Keeping
        # If we're adding to an existing row, we need to change that row's width.
        if row < len(rows):
            rows[row] = (rows[row][0] + width, rows[row][1])
        # If we're adding a new row, we need to append it.
        else:
            rows.append((width, totalHeight))
            totalHeight = totalHeight + height
        # Place the box at the coordinate
        placement.append({'id': dictionary['id'], 'place': coordinate})             # insert tuple at front of list
        # Reset the shortest row to 0 so the algorithm looks for the shortest row.
        shortestRow = 0
    # Sort the placements by ID so the driver gets the right placements for the right boxes.
    placement.sort(key=lambda dict: dict['id'])
    # Give the output back without the extra hash information.
    output = []
    for dictionary in placement:
        output.append(dictionary['place'])
    return output
