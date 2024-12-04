import re

file = open("Data_Day4_Test.txt", "r")
horizontal = file.readlines()
file.close()


# Part 1:
def findDiagonals(matrix):
    n = len(matrix)
    m = len(matrix[0])

    diagonals = []

    # Get top right to bottom left diagonals
    for d in range(n + m - 1):
        diagonal = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            j = d - i
            print("d: " + str(d))
            print("row: " + str(i))
            print("column: " + str(j))
            # Get the value at indexes i and j
            diagonal.append(matrix[i][j])
            print(diagonal)
        # Add diagonal to list of diagonals
        diagonals.append(''.join(diagonal))

        # Get top left to bottom right diagonals
    for d in range(n + m - 1):
        diagonal = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            j = m - 1 - (d - i)
            print("d: " + str(d))
            print("row: " + str(i))
            print("column: " + str(j))
            # Get the value at the intersection of i and j
            diagonal.append(matrix[i][j])
            print(diagonal)
        # Add diagonal to list of diagonals
        diagonals.append(''.join(diagonal))
    return diagonals


# Strip the newline character from the end of each list in horizontal
horizontal = [line.rstrip("\n") for line in horizontal]
# Split the lists into individual characters to get the vertical rows
split_chars = [list(char) for char in horizontal]
# Transpose split_chars so columns become rows
vertical_list = list(map(list, zip(*split_chars)))
# Join the lists so that each row is a single string
vertical = ["".join(sublist) for sublist in vertical_list]
# Create a matrix of values to get diagonals
matrix_text = [list(row) for row in horizontal]

# Initialize XMAS count
xmas_count = 0
# Find horizontal instances of XMAS in Word Search
# Use RegEx to find instances of XMAS or SAMX with lookahead to detect XMASAMX instances
for line in horizontal:
    xmas_count += len(re.findall(r'(?=(XMAS|SAMX))', line))
# print(xmas_count)
# Find vertical instances of XMAS in Word Search
for line in vertical:
    xmas_count += len(re.findall(r'(?=(XMAS|SAMX))', line))
# print(xmas_count)

# Get diagonals
diagonal = findDiagonals(matrix_text)
# Find diagonal instances of XMAS in Word Search
for line in diagonal:
    xmas_count += len(re.findall(r'(?=(XMAS|SAMX))', line))
# Print the total number of XMAS found in Part 1
print(xmas_count)


def findX_MAS(matrix):
    # Get number of rows
    n = len(matrix)
    # Get number of columns
    m = len(matrix[0])
    # Initialize xmas_count
    xmas_count = 0
    # Iterate over the rows and columns without checking the first/last row & columns
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            # Check if the target value is 'A'
            if matrix_text[i][j] == 'A':
                # Get values for the corners around 'A' and save the values
                tl = matrix_text[i - 1][j - 1]
                tr = matrix_text[i - 1][j + 1]
                bl = matrix_text[i + 1][j - 1]
                br = matrix_text[i + 1][j + 1]
                # Check that the corners are M or S and not equal to the diagonal corner
                if ((tl == "M" or tl == "S") and (br == "M" or br == "S") and tl != br) and \
                    ((tr == "M" or tr == "S") and(bl == "M" or bl == "S") and tr != bl): \
                    # Increment xmas_count and continue
                    xmas_count += 1
                else:
                    # 'A' not found, continue to next letter in the row
                    continue
    # Print the number of X-MAS found
    return print(xmas_count)


findX_MAS(matrix_text)
