import pandas as pd
df = pd.read_excel("Data_Day2.xlsx", sheet_name="Sheet1", header = None)


def nuclearSafety(df):
    unsafe = 0
    for i in range(0, len(df)):
        listRow = df.iloc[i].dropna().to_list()
        inc = listRow.copy()
        inc.sort()
        dec = listRow.copy()
        dec.sort(reverse=True)
        if listRow == inc or listRow == dec:
            for k in range(0, len(listRow) - 1):
                if 0 == abs(listRow[k] - listRow[k + 1]) or abs(listRow[k] - listRow[k + 1]) > 3:
                    # print("Consecutive values are equal too far apart")
                    unsafe += 1
                    break
                else:
                    continue
        else:
            # print("List is not increasing or decreasing")
            unsafe += 1

    print("Number of unsave values in list: " + str(unsafe))
    print("Number of safe values in list: " + str(len(df) - unsafe))
    print("Total rows: " + str(len(df)))


nuclearSafety(df)


# for i in range(0, 10):
#     unsafe = 0
#     listRow = df.iloc[i].dropna().to_list()
#     errorCount = 0
#     errorIndex = []
#     inc = listRow.copy()
#     inc.sort()
#     dec = listRow.copy()
#     dec.sort(reverse=True)
#     if listRow == inc:
#         print("List is increasing.")
#         for k in range(0, len(listRow) - 1):
#             if 0 < listRow[k + 1] - listRow[k] <= 3:
#                 continue
#             else:
#                 errorCount += 1
#                 errorIndex.append(k)
#     elif listRow == dec:
#         print("List is decreasing.")
#         for k in range(0, len(listRow) - 1):
#             if 0 < listRow[k] - listRow[k + 1] <= 3:
#                 continue
#             else:
#                 errorCount += 1
#                 errorIndex.append(k)
#     else:
#         print("List is not increasing or decreasing")
#     if errorCount >= 3:
#         continue
#     elif errorCount == 2:
#         for j in range(0, len(errorIndex)):
#             listRowCopy = listRow.copy()
#             listRowCopy.pop(errorIndex[j])
#
#
# print("Number of unsave values in list: " + str(unsafe))
# print("Number of safe values in list: " + str(len(df) - unsafe))
# print("Total rows: " + str(len(df)))



