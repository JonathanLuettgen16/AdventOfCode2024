from itertools import repeat


def importData():
    file = open("Data_Day9.txt", "r")
    data = file.read()
    file.close()
    return data


def createFileBlocksPart1(input_data):
    i = 0
    file_blocks = []
    for location in range(len(input_data)):
        value = input_data[location]
        if location % 2 == 0:
            file_blocks.append(list(repeat(i, int(value))))
            i += 1
        else:
            file_blocks.append(list(repeat('.', int(value))))
    file_blocks = [item for sublist in file_blocks for item in sublist]
    return file_blocks


def createFileBlocksPart2(input_data):
    i = 0
    file_blocks = []
    space_blocks = []
    for location in range(len(input_data)):
        value = input_data[location]
        if location % 2 == 0:
            file_blocks.append(list(repeat(i, int(value))))
            i += 1
        else:
            space_blocks.append(list(repeat('.', int(value))))
    file_length_list = [len(sublist) for sublist in file_blocks]
    space_length_list = [len(sublist) for sublist in space_blocks]
    return file_blocks, file_length_list, space_blocks, space_length_list


def swapFilesPart1(file_block_list):
    k = 0
    j = len(file_block_list) - 1
    while k < j:
        # print(k)
        if file_block_list[k] == '.':
            while file_block_list[j] == '.':
                if j == k:
                    print("j and k are equal")
                    break
                j -= 1
            file_block_list[k], file_block_list[j] = file_block_list[j], file_block_list[k]
        k += 1
    return file_block_list


def calculateCheckSum(file_reordered_list):
    file_reordered_list = [file for file in file_reordered_list if file != '.']
    rolling_value = 0
    for i, value in enumerate(file_reordered_list):
        rolling_value += i * value
    return rolling_value


def aocDay9Part1():
    data = importData()
    file_storage = createFileBlocksPart1(data)
    file_reordered = swapFilesPart1(file_storage)
    part1 = calculateCheckSum(file_reordered)
    return print(part1)


def flattenList(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flattenList(item))
        else:
            flat_list.append(item)
    return flat_list


data = importData()
fb, fll, sb, sll = createFileBlocksPart2(data)
# fb = fb[:15]
# fll = fll[:15]
# sb = sb[:15]
# sll = sll[:15]
empties = [[] for _ in range(len(fb))]
replacements = [[] for _ in range(len(fb))]


k = len(fb) - 1
while k >= 0:
    current_file_length = fll[k]
    current_file_section = fb[k]
    # print(current_file_length)
    # print(current_file_section)
    for i in range(k):
        if sll[i] >= current_file_length:
            # print("Files from the end of the list inserted into open position: " + str(i))
            # print("Modifying file lengths ")
            sll[i] -= fll[k]
            empties[i].append([val for val in list(repeat(fb[k][0], fll[k]))])
            # print(empties[i])
            sb[i] = sb[i][current_file_length:]
            fb.pop(k)
            fb.insert(k, [])
            replacements[k].append([val for val in list(repeat('.', fll[k]))])
            fll[k] = 0
            break
    # print("fb = " + str(fb))
    # print("fll = " + str(fll))
    # print("sb = " + str(sb))
    # print("sll = " + str(sll))
    k -= 1


merged_list = []
# print(sb)
# print(len(sb))
# print(fb)
# print(len(fb))
# print(empties)
# print(len(empties))
# print(replacements)
# print(len(replacements))
for i in range(len(empties)):
    try:
        merged_list.append(fb[i])
        merged_list.append(replacements[i])
        merged_list.append(empties[i])
        merged_list.append(sb[i])
    except:
        print(i)
merged_list_flat = flattenList(merged_list)
# print(merged_list_flat)
rolling_value = 0
for i, value in enumerate(merged_list_flat):
    if value != '.':
        rolling_value += i * value
    else:
        continue
print(rolling_value)
