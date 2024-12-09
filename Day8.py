def buildMatrix(input_data):
    # Create a matrix where each coordinate in the matrix is a single value
    return [list(row) for row in input_data]


def buildNodeDictionary(input_matrix):
    # Initialize an empty dictionary
    node_dictionary = {}
    # Iterate over the rows of the matrix
    for i in range(len(input_matrix)):
        # Iterate over the columns of the matrix
        for j in range(len(input_matrix[0])):
            # Save the current character of the (i, j) coordinate pair
            char = input_matrix[i][j]
            # Check if the variable is not a period
            if char != '.':
                # Check if the character is already a key in the dictionary
                if char in node_dictionary.keys():
                    # Append the coordinates of the character to the list of other coordinates for the character
                    node_dictionary[char].append((i, j))
                else:
                    # Create a new dictionary key and set the value to the coordinates of the character
                    node_dictionary[char] = [(i, j)]
    # Output the antennae dictionary
    return node_dictionary


def calculateAntiNodesPart1(a, b, x_max, y_max):
    # Initialize the values of c and d (outputs) as nothing
    c = None
    d = None
    # Set initial conditions
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    # Calculate row/column difference between two nodes
    dx, dy = x1 - x2, y1 - y2
    # If the new values are in the bounds of the matrix, save them to c and d
    if 0 <= x1 + dx < x_max and 0 <= y1 + dy < y_max:
        c = (x1 + dx, y1 + dy)
    if 0 <= x2 - dx < x_max and 0 <= y2 - dy < y_max:
        d = (x2 - dx, y2 - dy)
    # Output c and d to the outer function
    return c, d


def aocDay8Part1():
    file = open("Data_Day8.txt", "r")
    data = file.read().splitlines()
    file.close()
    matrix = buildMatrix(data)
    x_max = len(matrix)
    y_max = len(matrix[0])
    node_dict = buildNodeDictionary(matrix)
    # Initialize an empty list of anti-nodes
    anti_node_list = []
    # Iterate through the key: value pairs in the dictionary
    for key in node_dict:
        value = node_dict.get(key)
        # Iterate over the coordinate locations as loc1
        for k, loc1 in enumerate(value):
            # Create a new list of coordinates to compare. Since the calculateAntiNodesPart1 function operates
            # in both directions, we only need to compare loc1 with locations after it in the value part of the
            # dictionary
            for loc2 in value[k + 1:]:
                a1, a2 = calculateAntiNodesPart1(loc1, loc2, x_max, y_max)
                # Check if a1 (anti-node 1) is None [outside the bounds] or already in the list
                if a1 is not None and a1 not in anti_node_list:
                    # Add valid & non-repeated value to the anti-node list
                    anti_node_list.append(a1)
                # Check if a2 (anti-node 2) is None [outside the bounds] or already in the list
                if a2 is not None and a2 not in anti_node_list:
                    # Add valid & non-repeated value to the anti-node list
                    anti_node_list.append(a2)
    # Print the answer to Part 1 to the console
    return print(len(anti_node_list))


def calculateAntiNodesPart2(a, b, x_max, y_max):
    # Initialize each node to the anti-node list
    anti_node_list = [a, b]
    # Set initial conditions
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    # Calculate row/column differences between nodes
    dx, dy = x1 - x2, y1 - y2
    # Repeat as long as the value of x1 + dx and y1 + dy are within bounds of the matrix
    while 0 <= x1 + dx < x_max and 0 <= y1 + dy < y_max:
        c = (x1 + dx, y1 + dy)
        # Ensure no duplicates in the anti_node_list
        if c not in anti_node_list:
            anti_node_list.append(c)
        # Increment x1 and y1 by dx and dy
        x1 += dx
        y1 += dy
    # Once the outer boundary is reached, reset x1 and y1 to the first input location's coordinates for the second
    # direction
    x1, y1 = a[0], a[1]
    # Repeat as long as the value of x1 - dx and y1 - dy are within the boundaries of the matrix
    while 0 <= x1 - dx < x_max and 0 <= y1 - dy < y_max:
        d = (x1 - dx, y1 - dy)
        # Ensure no duplicates in the anti_node_list
        if d not in anti_node_list:
            anti_node_list.append(d)
        # Decrement x1 and y1 by dx and dy
        x1 -= dx
        y1 -= dy
    # Output the anti-node list to the outer function
    return anti_node_list


def aocDay8Part2():
    file = open("Data_Day8.txt", "r")
    data = file.read().splitlines()
    file.close()
    matrix = buildMatrix(data)
    x_max = len(matrix)
    y_max = len(matrix[0])
    node_dict = buildNodeDictionary(matrix)
    # Initialize an empty anti_node_list
    anti_node_list = []
    for key in node_dict:
        value = node_dict.get(key)
        for k, loc1 in enumerate(value):
            for loc2 in value[k + 1:]:
                # Append the sublist from calculateAntiNodesPart2 to the main anti_node_list
                anti_node_list.append(calculateAntiNodesPart2(loc1, loc2, x_max, y_max))
    # Flatten the list of lists and ensure no repeats of coordinates. Print the answer to Part 2
    return print(len(set([coordinates for sublist in anti_node_list for coordinates in sublist])))


aocDay8Part1()
aocDay8Part2()





