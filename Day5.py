file = open("Data_Day5.txt", "r")
data = file.readlines()
file.close()

# Strip the newlines from the text
data = [line.rstrip("\n") for line in data]
# Sort the text into rules and manuals using the proper delimiters
rules = [line for line in data if "|" in line]
manuals = [line for line in data if "," in line]
# print(rules)
# print(manuals)

# Split the list of rules into tuples for processing into the dictionary
rules_split = [tuple(map(str, val.split("|"))) for val in rules]
# print(rules_split)
# Split the list of manuals into single values in each list
manuals_split = [list(map(str, val.split(","))) for val in manuals]
# print(manuals_split)

"""
In Part 1 I created a reverse lookup dictionary to check the list of previously printed
pages for values that can't be printed before the current page. This code is all commented
out because in Part 2 I needed the key:value pairs in the dictionary to be switched.
I'm leaving this code in for when I look back at this later."""

# Part 1
# def createRuleDictionary(list):
#     ruleDict = {}
#     for value, key in list:
#         if key in ruleDict:
#             ruleDict[key].append(value)
#         else:
#             ruleDict[key] = [value]
#     return ruleDict


#rule_dict = createRuleDictionary(rules_split)
# print(rule_dict)


def intersection(list1, list2):
    if list1 != None:
        list3 = [value for value in list1 if value in list2]
    else:
        list3 = []
    return list3


# def part1Jobs(manuals, rule_dict):
#     printed_manuals = []
#     middle_page_sum = 0
#     for manual in manuals:
#         printed_pages = []
#         ineligible_pages = set()
#         for page in manual:
#             if page in ineligible_pages:
#                 print("Page ineligible to print: " + page)
#                 break
#             else:
#                 printed_pages.append(page)
#                 if rule_dict.get(page) != None:
#                     for val in rule_dict.get(page):
#                         ineligible_pages.add(val)
#         if len(printed_pages) == len(manual):
#             printed_manuals.append(manual)
#             middle_page_sum += int(manual[int((len(manual) - 1)/2)])
#     return print(middle_page_sum)
#
#
# part1Jobs(manuals_split, rule_dict)


# Part 2
# Create the key:value pair dictionary for Part 2
def createRuleDictionary(list):
    ruleDict = {}
    for key, value in list:
        if key in ruleDict:
            ruleDict[key].append(value)
        else:
            ruleDict[key] = [value]
    return ruleDict


rule_dict = createRuleDictionary(rules_split)

# Define function to solve Part 2 (and Part 1)
def part2Jobs(manuals, rule_dict):
    # Initialize empty lists and zero sums for use later
    printed_manuals = []
    error_manuals = []
    printed_middle_page_sum = 0
    error_middle_page_sum = 0
    # Iterate over each manual
    for manual in manuals:
        # Initialize an empty list to store previously printed pages
        printed_pages = []
        # Initialize print error to be false (used to sort manuals I change vs. manuals in correct order)
        print_error = False
        # Iterate over each page of the manual
        for x, page in enumerate(manual):
            # Check to see if there is an intersection between previously printed pages
            # and pages that must be after the current page
            if len(intersection(rule_dict.get(page), printed_pages)) > 0:
                print_error = True
                # print("Could not print page: " + page)
                # print("Previously printed pages: " + str(printed_pages))
                # Iterate through the previously printed pages to find which page caused the error.
                for val in printed_pages:
                    if val in rule_dict.get(page):
                        # print("Cause of the error: " + val)
                        # print("Index of the error: " + str(printed_pages.index(val)))
                        # Get the index of the page that caused the error and break the loop
                        y = printed_pages.index(val)
                        break
                # Insert the current page in front of the page that caused the error
                printed_pages.insert(y, page)
                # print(printed_pages)
            else:
                # If the page passes the order test, append it to the end of the printed pages
                printed_pages.append(page)
        # At the end of a manual, if there was an error, append the list of printed pages (which has been reordered)
        # to the error manuals list
        if print_error == True:
            error_manuals.append(printed_pages)
            # Get the middle value and add it to the rolling sum of middle pages for the error manuals
            error_middle_page_sum += int(printed_pages[int((len(printed_pages) - 1)/2)])
        # If pages are already in the correct order, append the list of printed pages to the printed manuals list
        # This is the solution to Part 1
        else:
            printed_manuals.append(printed_pages)
            # Get the middle value and add it to the rolling sum of middle pages for the printed manuals
            printed_middle_page_sum += int(printed_pages[int((len(printed_pages) - 1)/2)])
    return printed_middle_page_sum, error_middle_page_sum


part1, part2 = part2Jobs(manuals_split, rule_dict)
print(part1)
print(part2)