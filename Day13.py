def parseData(input_data, part: int):
    # Initialize empty matrix and constants
    matrix = []
    constants = []
    # Get Button A, Button B, and Target Values from input data
    buttonA_list = [item.strip('\n').strip("Button A: ").split(', ') for item in input_data if "Button A:" in item]
    buttonB_list = [item.strip('\n').strip("Button B: ").split(', ') for item in input_data if "Button B:" in item]
    targets = [item.strip('\n').strip("Prize: ").split(', ') for item in input_data if "Prize:" in item]
    # Split lists into xa, xb, xt, ya, yb, yt lists
    xa = [int(item.split('+')[1]) for sublist in buttonA_list for item in sublist if 'X' in item]
    xb = [int(item.split('+')[1]) for sublist in buttonB_list for item in sublist if 'X' in item]
    ya = [int(item.split('+')[1]) for sublist in buttonA_list for item in sublist if 'Y' in item]
    yb = [int(item.split('+')[1]) for sublist in buttonB_list for item in sublist if 'Y' in item]
    if part == 1:
        xt = [int(item.split('=')[1]) for sublist in targets for item in sublist if 'X' in item]
        yt = [int(item.split('=')[1]) for sublist in targets for item in sublist if 'Y' in item]
    else:
        xt = [int(item.split('=')[1]) + 10000000000000 for sublist in targets for item in sublist if 'X' in item]
        yt = [int(item.split('=')[1]) + 10000000000000 for sublist in targets for item in sublist if 'Y' in item]
    for x1, x2, y1, y2, t1, t2 in zip(xa, xb, ya, yb, xt, yt):
        matrix.append([[x1, x2], [y1, y2]])
        constants.append([[t1], [t2]])
    return matrix, constants


def calculateMoves(X, C):
    # Calculate the number of moves from A and number of moves from B and ensure integers
    a = (X[1][1]*C[0][0] - C[1][0]*X[0][1]) // (X[0][0]*X[1][1] - X[0][1]*X[1][0])
    b = (-X[1][0]*C[0][0] + C[1][0]*X[0][0]) // (X[0][0]*X[1][1] - X[0][1]*X[1][0])
    # Check that integer solution works for the problem at hand
    if X[0][0]*a + X[0][1]*b == C[0][0] and X[1][0]*a + X[1][1]*b == C[1][0]:
        return 3*a + b
    else:
        return 0


def part1(in_data):
    left_matrix, right_matrix = parseData(in_data, 1)
    token_count = 0
    for left, right in left_matrix, right_matrix:
        token_count += calculateMoves(left, right)
    return print(f"Part 1 solution is {token_count}")


def part2(in_data):
    left_matrix, right_matrix = parseData(in_data, 2)
    token_count = 0
    for left, right in left_matrix, right_matrix:
        token_count += calculateMoves(left, right)
    return print(f"Part 2 solution is {token_count}")


file = open("Data_Day13.txt", "r")
data = file.readlines()

part1(data)
part2(data)