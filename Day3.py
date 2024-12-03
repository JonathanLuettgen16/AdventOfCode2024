import re

file = open("Data_Day3.txt", "r")
text = file.read()
file.close()
# print(text)


# Part 1
def parseText(text):
    # Find match for "mul(", 1-3 digit number, ", " 1-3 digit number, ")" and return tuples with the numbers as strings
    targetlist = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)
    # print(len(targetlist))
    # print(targetlist)
    # Return the product of the strings as integers and sum the products over the list
    return sum([int(val1) * int(val2) for val1, val2 in targetlist])


# Print the result of Part 1
print(parseText(text))


# Part 2
def parseDoAndDont(text):
    # Find "do()", the mul() targets from earlier, and "don't()" in the text
    matches = re.findall(r'(do\(\)|mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\))', text)
    # Join the values returned as tuples in matches, into a string for further manipulation
    filteredText = " ".join(match[0] if match[0] else f'mul({match[1]}, {match[2]})' for match in matches)
    # print(filteredText)
    # Remove any text from filteredText that is between a "don't()" and a "do()"
    cleanedText = re.sub(r"don't\(\).*?do\(\)", "", filteredText)
    # Remove any text from cleanedText that is after the final "don't()"
    cleanedFinalDont = re.sub(r"don't\(\).*", "", cleanedText)
    # Run the original function on the cleanedFinalDont text
    return parseText(cleanedFinalDont)


# Print the result of Part 2
print(parseDoAndDont(text))
