import pandas as pd

ex_path = r"C:\Users\fisch\Desktop\projects\efly\efly_scrape\lead_neu (31).xlsx"

ex = pd.read_excel(ex_path, sheet_name="Sheet1")

ex = ex.fillna("noVal")

# print(ex.columns.values)
#
# for row in ex[["Händler-Info2"]].to_numpy()[10:20]:
#     if row[0] == "noVal":
#     print(row[0])
#         continue

print(ex.iloc[19]["Händler-Info2"])