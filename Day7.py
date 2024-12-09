from itertools import product

file = open("Data_Day7.txt", "r")
data = file.read().splitlines()
file.close()

# print(data)

"""
This section is the non-optimized code that got me to an initial solution. Further below is a more optimized approach
"""


# def parseData(data_input):
#     targets = [int(item.split(": ")[0]) for item in data_input]
#     values = [[int(value) for value in item.split(": ")[1].split(" ")] for item in data_input]
#     return targets, values
#
#
# def add(a , b):
#     return a + b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def combine(a, b):
#     return int(str(a) + str(b))
#
#
# def get_perms(length):
#     perms = list(product(['add', 'multiply', '||'], repeat = (length - 1)))
#     perms = [list(perm) for perm in perms]
#     return perms
#
#
# def part1(data_input):
#     targets, values = parseData(data_input)
#     part1_solution = 0
#     for target, value in zip(targets, values):
#         perms = get_perms(len(value))
#         for operations in perms:
#             rolling_value = value[0]
#             for op, val in zip(operations, value[1:]):
#                 if op == 'add':
#                     rolling_value = add(rolling_value, val)
#                 elif op == 'multiply':
#                     rolling_value = multiply(rolling_value, val)
#                 elif op == '||':
#                     rolling_value = combine(rolling_value, val)
#             if rolling_value == target:
#                 print("Rolling value equals target for: " + str(target))
#                 part1_solution += rolling_value
#                 break
#     return print(part1_solution)
#
#
# # targets = [int(item.split(": ")[0]) for item in data]
# # values = [[int(value) for value in item.split(": ")[1].split(" ")] for item in data]
# # values = [item.split(": ")[1] for item in data]
# # values_split = [item.split(" ") for item in values]
# # int_values = [[int(value) for value in sublist] for sublist in values_split]
#
# # targets, values = parseData(data)
# # print(len(targets))
#
#
# # print(targets)
# # print(values)
#
# # length_of_values = 3
# #
# # perm_list = get_perms(length_of_values)
# # print(perm_list)
#
# part1(data)


"""
Begin code optimization
"""


def parseData(data_input):
    targets = [int(item.split(": ")[0]) for item in data_input]
    values = [[int(value) for value in item.split(": ")[1].split(" ")] for item in data_input]
    return targets, values


def operate(a, b, operator):
    if operator == 'add':
        return a + b
    elif operator == 'multiply':
        return a * b
    elif operator == '||':
        return int(str(a) + str(b))
    else:
        raise Exception("Operator not found")


def createOperatorsDict(max_length, ops_list):
    opsDict = {}
    for i in range(2, max_length + 1):
        opsDict[i] = [list(operator) for operator in list(product(ops_list, repeat=(i - 1)))]
    return opsDict


def aocDay7(data_input, problem_operators):
    targets, values = parseData(data_input)
    solution = 0
    max_list_length = max([len(value) for value in values])
    ops_dict = createOperatorsDict(max_list_length, problem_operators)
    for target, value in zip(targets, values):
        operators = ops_dict.get(len(value))
        for operations in operators:
            rolling_value = value[0]
            for op, val in zip(operations, value[1:]):
                rolling_value = operate(rolling_value, val, op)
            if rolling_value == target:
                solution += rolling_value
                break
    return print(solution)


aocDay7(data, ['add', 'multiply'])
aocDay7(data, ['add', 'multiply', '||'])
