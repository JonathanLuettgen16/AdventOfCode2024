file = open("Data_Day11.txt", "r")
data = file.read().split(' ')
file.close()
data_p1 = [[int(val)] for val in data]
data_p2 = [int(val) for val in data]

"""
This section marks before I knew that keeping the position of the stones was important...
"""

def stoneRules(item):
    if item[0] == 0:
        item[0] = 1
    else:
        item_length = len(str(item[0]))
        if item_length % 2 == 0:
            item.append(int(str(item[0])[int(item_length / 2):]))
            item[0] = int(str(item[0])[:int(item_length / 2)])
        else:
            item[0] *= 2024
    return item


# Part 1 solution: Loop over the values in the list and then re-flatten so that each item
# in the list is a single element list
for i in range(0, 25):
    for value in data_p1:
        stoneRules(value)
    data_p1 = [[item] for sublist in data_p1 for item in sublist]

# Fully flatten the list of stones after 25 iterations
data_p1 = [item for sublist in data_p1 for item in sublist]
print(f"Part 1 solution = {len(data_p1)}")


# Part 2 required a different approach because the list I used in part 1 would grow unreasonably long
def blink(input_dict: dict):
    # Check if 0 was in the list of keys and bump those values to 1 to initialize the second dictionary
    if 0 in input_dict.keys():
        new_blink_dict = {1: input_dict.get(0)}
        # Remove 0 from the old dictionary so we don't iterate over it again
        del input_dict[0]
    else:
        # Initialize a blank dictionary
        new_blink_dict = {}

    # Iterate over the keys and apply rules 2 and 3 to each key, while using the values from the old dictionary
    for key, val in input_dict.items():
        key_length = len(str(key))
        if key_length % 2 == 0:
            left_key, right_key = int(str(key)[:int(key_length / 2)]), int(str(key)[int(key_length / 2):])
            if left_key in new_blink_dict.keys():
                # Check if left_key already exists in the new dictionary and increment existing value
                new_blink_dict[left_key] += val
            else:
                # Create new key: value pair when key not in the dictionary
                new_blink_dict[left_key] = val
            if right_key in new_blink_dict.keys():
                # Check if right_key already exists in the new dictionary and increment existing value
                new_blink_dict[right_key] += val
            else:
                new_blink_dict[right_key] = val
        else:
            # Apply rule 3 to keys with odd number lengths
            new_blink_dict[int(key) * 2024] = val
    # Return the new dictionary
    return new_blink_dict

# Initialize the dictionary
stone_count_dict = {}
for val in data_p2:
    if val in stone_count_dict.keys():
        stone_count_dict[val] = stone_count_dict.get(val) + 1
    else:
        stone_count_dict[val] = 1

# Iterate number of times required for Part 2, and print Part 1 solution on the way
for i in range(75):
    if i == 25:
        print(sum(stone_count_dict.values()))
    stone_count_dict = blink(stone_count_dict)

print(sum(stone_count_dict.values()))
