warehouse = open("Data_Day15_Warehouse.txt", "r").read().splitlines()
warehouse = [list(row) for row in warehouse]

movements = open("Data_Day15_Movements.txt", 'r').read()
movements = [char for char in movements if char != '\n']


def east(current_loc, matrix):
    push = matrix[current_loc[0]][current_loc[1] + 1:]
    push = push[:push.index('#')]
    if len(push) == 0 or '.' not in push:
        # print("Robot is against a wall or there is no room to push crates")
        return current_loc, matrix
    elif push[0] == '.':
        # print("Robot's next square is empty. Advancing the robot east by 1")
        matrix[current_loc[0]][current_loc[1]] = '.'
        current_loc = (current_loc[0], current_loc[1] + 1)
        matrix[current_loc[0]][current_loc[1]] = '@'
        return current_loc, matrix
    elif push[0] == 'O':
        # print("Robot is able to push a crate.")
        counter = 1
        while push[counter] == 'O':
            counter += 1
        # print(f"There are {counter} crates in a row to push")
        matrix[current_loc[0]][current_loc[1]] = '.'
        matrix[current_loc[0]][current_loc[1] + 1] = '@'
        matrix[current_loc[0]][current_loc[1] + counter + 1] = 'O'
        current_loc = (current_loc[0], current_loc[1] + 1)
        return current_loc, matrix


def west(current_loc, matrix):
    push = matrix[current_loc[0]][current_loc[1]-1::-1]
    push = push[:push.index('#')]
    if len(push) == 0 or '.' not in push:
        # print("Robot is against a wall or there is no room to push crates.")
        return current_loc, matrix
    elif push[0] == '.':
        # print("Robot's next square is empty. Advancing the robot east by 1")
        matrix[current_loc[0]][current_loc[1]] = '.'
        current_loc = (current_loc[0], current_loc[1] - 1)
        matrix[current_loc[0]][current_loc[1]] = '@'
        return current_loc, matrix
    elif push[0] == 'O':
        # print("Robot is able to push a crate.")
        counter = 1
        while push[counter] == 'O':
            counter += 1
        # print(f"There are {counter} crates in a row to push")
        matrix[current_loc[0]][current_loc[1]] = '.'
        matrix[current_loc[0]][current_loc[1] - 1] = '@'
        matrix[current_loc[0]][current_loc[1] - counter - 1] = 'O'
        current_loc = (current_loc[0], current_loc[1] - 1)
        return current_loc, matrix


def north(current_loc, matrix):
    push = [matrix[i][current_loc[1]] for i in range(current_loc[0])]
    push.reverse()
    push = push[:push.index('#')]
    if len(push) == 0 or '.' not in push:
        # print("Robot is against a wall or there is no room to push crates.")
        return current_loc, matrix
    elif push[0] == '.':
        # print("Robot's next square is empty. Advancing the robot east by 1")
        matrix[current_loc[0]][current_loc[1]] = '.'
        current_loc = (current_loc[0] - 1, current_loc[1])
        matrix[current_loc[0]][current_loc[1]] = '@'
        return current_loc, matrix
    elif push[0] == 'O':
        # print("Robot is able to push a crate.")
        counter = 1
        while push[counter] == 'O':
            counter += 1
        # print(f"There are {counter} crates in a row to push")
        matrix[current_loc[0]][current_loc[1]] = '.'
        matrix[current_loc[0] - 1][current_loc[1]] = '@'
        matrix[current_loc[0] - counter - 1][current_loc[1]] = 'O'
        current_loc = (current_loc[0] - 1, current_loc[1])
        return current_loc, matrix


def south(current_loc, matrix):
    push = [matrix[i][current_loc[1]] for i in range(current_loc[0] + 1, len(matrix))]
    push = push[:push.index('#')]
    if len(push) == 0 or '.' not in push:
        # print("Robot is against a wall or there is no room to push crates.")
        return current_loc, matrix
    elif push[0] == '.':
        # print("Robot's next square is empty. Advancing the robot east by 1")
        matrix[current_loc[0]][current_loc[1]] = '.'
        current_loc = (current_loc[0] + 1, current_loc[1])
        matrix[current_loc[0]][current_loc[1]] = '@'
        return current_loc, matrix
    elif push[0] == 'O':
        # print("Robot is able to push a crate.")
        counter = 1
        while push[counter] == 'O':
            counter += 1
        # print(f"There are {counter} crates in a row to push")
        matrix[current_loc[0]][current_loc[1]] = '.'
        matrix[current_loc[0] + 1][current_loc[1]] = '@'
        matrix[current_loc[0] + counter + 1][current_loc[1]] = 'O'
        current_loc = (current_loc[0] + 1, current_loc[1])
        return current_loc, matrix


robot_loc = (0, 0)
for y, row in enumerate(warehouse):
    if '@' in row:
        x = row.index('@')
        robot_loc = (x, y)
        break
print(robot_loc)
# for row in warehouse:
#     print(''.join(row))

for i, direction in enumerate(movements):
    if direction == '^':
        # print("North")
        robot_loc, warehouse = north(robot_loc, warehouse)
    elif direction == '>':
        # print("East")
        robot_loc, warehouse = east(robot_loc, warehouse)
    elif direction == 'v':
        # print("South")
        robot_loc, warehouse = south(robot_loc, warehouse)
    else:
        # print("West")
        robot_loc, warehouse = west(robot_loc, warehouse)


gps_sum = 0
for y, row in enumerate(warehouse):
    for x, char in enumerate(row):
        if char == 'O':
            gps_sum += 100*y + x

print(gps_sum)
