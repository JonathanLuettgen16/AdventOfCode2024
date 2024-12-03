import pandas as pd
df = pd.read_excel("Data_Day2.xlsx", sheet_name="Sheet1", header = None)


def strictSafety(row):
    delta = [b - a for a, b in zip(row[:-1], row[1:])]
    if (min(delta) >= -3 and max(delta) <= -1) or (min(delta) >= 1 and max(delta) <= 3):
        return "safe"
    else:
        return "unsafe"


safetyResults = []
for i in range(len(df)):
    row = df.iloc[i].dropna().to_list()
    safetyResults.append(strictSafety(row))
print("Number of unsafe values: " + str(safetyResults.count("unsafe")))
print("Number of safe values: " + str(safetyResults.count("safe")))


def softSafety(row):
    strict = strictSafety(row)
    if strict == "safe":
        return "safe"
    else:
        dropOneSafety = []
        for k in range(len(row)):
            dropOneSafety.append(strictSafety(row[:k] + row[k + 1:]))
        if "safe" in dropOneSafety:
            return "safe"
        else:
            return "unsafe"


softSafetyResults = []
for i in range(len(df)):
    row = df.iloc[i].dropna().to_list()
    softSafetyResults.append(softSafety(row))
print("Number of soft unsafe values: " + str(softSafetyResults.count("unsafe")))
print("Number of soft safe values: " + str(softSafetyResults.count("safe")))
