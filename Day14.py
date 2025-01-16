# a = (2, 4)
# b = (2, -3)
#
# n = 7
# m = 11
# matrix = [['.' for _ in range(n)] for _ in range(m)]
#
#
#
#
# robot = moveRobot(a, b)
# matrix[robot[1]][robot[0]] = 'R'
# print(matrix)
from typing import Tuple


def moveRobot(k_x, k_y, l_x, l_y, boundary_x, boundary_y, seconds) -> Tuple[int, int]:
    return ((k_y + seconds * l_y) % boundary_y, (k_x + seconds * l_x) % boundary_x)


def splitQuadrants(end_coords, bound_x, bound_y):
    q1 = sum([1 for x, y in end_coords if x < bound_y // 2 and y < bound_x // 2])
    q2 = sum([1 for x, y, in end_coords if x > bound_y // 2 and y < bound_x // 2])
    q3 = sum([1 for x, y, in end_coords if x < bound_y // 2 and y > bound_x // 2])
    q4 = sum([1 for x, y in end_coords if x > bound_y // 2 and y > bound_x // 2])
    return q1 * q2 * q3 * q4



def part1(file_name, reps, bound_x = 11, bound_y = 7):
    file = open(file_name, "r")
    data = file.read().splitlines()
    end_locations = []
    for item in data:
        p_vals, v_vals = item.split(' v=')
        p_vals = p_vals.replace('p=', '')
        p_x, p_y = map(int, p_vals.split(','))
        v_x, v_y = map(int, v_vals.split(','))
        end_locations.append(moveRobot(p_x, p_y, v_x, v_y, bound_x, bound_y, reps))
    solution = splitQuadrants(end_locations, bound_x, bound_y)
    return print(solution)


part1("Data_Day14.txt", 100, 101, 103)
