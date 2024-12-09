file = open("Data_Day6.txt", "r")
data = file.readlines()
file.close()

data = [line.rstrip("\n") for line in data]


def getMatrix(list_of_lists):
    return [list(row) for row in list_of_lists]


def findGuard(matrix):
    # Iterate over enumerate(rows) to find the row index of the guard
    for x, row in enumerate(matrix):
        # If the guard is in the row, find the column index of the guard
        if '^' in row:
            return x, row.index('^')
        else:
            continue


def changeDirection(current_direction, matrix_operation = (-1, 0), obstacle = False):
    # If an obstacle is found in the matrix, turn the guard 90 degrees clockwise and
    # return the matrix operation needed for the next movement
    if current_direction == "north" and obstacle:
        return "east", (0, 1)
    elif current_direction == "east"and obstacle:
        return "south", (1, 0)
    elif current_direction == "south"and obstacle:
        return "west", (0, -1)
    elif current_direction == "west" and obstacle:
        return "north", (-1, 0)
    else:
        return current_direction, matrix_operation


def calculatePositionVisits(matrix):
    return sum([1 for row in matrix for val in row if val == "X"])


def guardMovement(matrix, n, m, currentDirection, path, matrix_operation):
    try:
        if not(0 <= n + matrix_operation[0] <= len(matrix)) or not(0 <= m + matrix_operation[1] <= len(matrix[0])):
            raise Exception("Next value is out of bounds")
        next_location = matrix[n + matrix_operation[0]][m + matrix_operation[1]]
        if next_location == "#":
            # print("Obstacle found at " + str(n + matrix_operation[0]) + " , " + str(m + matrix_operation[1]))
            # print("Current direction is: " + currentDirection)
            path.append((currentDirection, (n, m)))
            currentDirection, matrix_operation = changeDirection(currentDirection, matrix_operation, True)
            # print("New direction is: " + currentDirection)
        else:
            path.append((currentDirection, (n, m)))
            matrix[n][m] = "X"
            n += matrix_operation[0]
            m += matrix_operation[1]
            # for row in matrix:
            #     print(''.join(row))
    except:
        matrix[n][m] = "X"
        path.append((currentDirection, (n, m)))
        print("Edge of puzzle reached")
        print("Guard Exited the puzzle at row " + str(n) + " column " + str(m))
        # for row in matrix:
        #     print(''.join(row))
        print(calculatePositionVisits(matrix))
        return matrix, n, m, currentDirection, matrix_operation, True, path
    return matrix, n, m, currentDirection, matrix_operation, False, path


def part1():
    data_matrix = getMatrix(data)
    x, y = findGuard(data_matrix)
    print(f"Guard found in row: {x}, column: {y}.")
    direction = "north"
    operation = (-1, 0)
    path = []
    end_of_puzzle = False
    while not(end_of_puzzle):
        data_matrix, x, y, direction, operation, end_of_puzzle, path = \
            guardMovement(data_matrix, x, y, direction, path, operation)
    print(path)


def check_loops(path: list):
    if len(path) > len(set(path)):
        return True
    else:
        return False


def part2():
    part2_solution = 0
    for barrier in possible_new_barriers:
        # Create new lab
        matrix = getMatrix(data)
        # Set initial conditions
        g1, g2 = findGuard(matrix)
        if (g1, g2) != barrier:
            matrix[barrier[0]][barrier[1]] = "#"
            loop = False
            exit_found = False
            direction = "north"
            operation = (-1, 0)
            path_walk = []
            # Walk guard through lab until one of two conditions is met: end_of_puzzle = True or loop = True
            while not (exit_found or loop):
                matrix, g1, g2, direction, operation, exit_found, path_walk = \
                    guardMovement(matrix, g1, g2, direction, path_walk, operation)
                loop = check_loops(path_walk)
                if loop:
                    part2_solution += 1
        else:
            print("Cannot print barrier over guard starting point")
    return print(part2_solution)

data_matrix = getMatrix(data)
n, m = findGuard(data_matrix)
print("Guard found in row " + str(n) + " column " + str(m))

end_Of_Puzzle = False
current_direction = "north"
matrix_operation = (-1, 0)
path = []
while not end_Of_Puzzle:
    data_matrix, n, m, current_direction, matrix_operation, end_Of_Puzzle, path = \
        guardMovement(data_matrix, n, m, current_direction, path, matrix_operation)


possible_new_barriers = set([val[1] for val in path])
# definite_barriers = [(6, 3), (7, 6), (7, 7), (8, 1), (8, 3), (9, 7)]
# print([val for val in definite_barriers if val in possible_new_barriers])

part2()

