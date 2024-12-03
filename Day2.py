import pandas as pd
df = pd.read_excel("Data_Day2.xlsx", sheet_name="Sheet1", header = None)

# Part 1
def strictSafety(row):
    # Create a list of the differences between consecutive indexes
    delta = [b - a for a, b in zip(row[:-1], row[1:])]
    # Verify that differences are all between -3 and -1 or 1 and 3
    if (min(delta) >= -3 and max(delta) <= -1) or (min(delta) >= 1 and max(delta) <= 3):
        return "safe"
    else:
        return "unsafe"


# Create empty list to store results from safety check
safetyResults = []
for i in range(len(df)):
    row = df.iloc[i].dropna().to_list()
    safetyResults.append(strictSafety(row))
# Print results
print("Number of unsafe values: " + str(safetyResults.count("unsafe")))
print("Number of safe values: " + str(safetyResults.count("safe")))

# Part 2
def softSafety(row):
    strict = strictSafety(row)
    if strict == "safe":
        return "safe"
    else:
        # Create empty list for storing results from soft safety checks
        dropOneSafety = []
        for k in range(len(row)):
            dropOneSafety.append(strictSafety(row[:k] + row[k + 1:]))
        if "safe" in dropOneSafety:
            return "safe"
        else:
            return "unsafe"

# Create empty list to to store results from soft safety check
softSafetyResults = []
for i in range(len(df)):
    row = df.iloc[i].dropna().to_list()
    softSafetyResults.append(softSafety(row))
# Print results from soft safety check
print("Number of soft unsafe values: " + str(softSafetyResults.count("unsafe")))
print("Number of soft safe values: " + str(softSafetyResults.count("safe")))
