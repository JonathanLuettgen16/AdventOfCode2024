"""
Challenge Day 1: Part 1
From two lists of integers:
 Sort the lists from smallest to largest
 Calculate the distance between each integer pair
 Calculate the total distance between each list.
Example:
 L1 = [3, 4, 2, 1, 3, 3]
 L2 = [4, 3, 5, 3, 9, 3]
 Answer = 11
"""

import pandas as pd

df = pd.read_excel("Data_Day1.xlsx", sheet_name="Sheet1")
left = df['List 1'].to_list()
right = df['List 2'].to_list()


def listdistance(list1, list2):
    list1.sort()
    list2.sort()
    list3 = [abs(x - y) for x, y in zip(list1, list2)]
    return sum(list3)


distance = listdistance(left, right)
print(distance)

"""
Challenge Day 1: Part 2
From two lists of integers:
 Determine how many times the value from L1 appear in L2
 Multiply the value from L1 with the number of appearances in L2
 Calculate the similarity score by adding up the resulting scores
Example:
 L1 = [3, 4, 2, 1, 3, 3]
 L2 = [4, 3, 5, 3, 9, 3]
 Answer = 31
"""


def listsimilarity(list1, list2):
    list1.sort()
    list3 = [x * list2.count(x) for x in list1]
    return sum(list3)


similarity = listsimilarity(left, right)
print(similarity)