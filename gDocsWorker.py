import xl_model
import pandas as pd
import gspread

gc = gspread.oauth()

file = gc.open_by_key("1RPZ81nHBtbSvuNCE3gtCa4Fc-KRBelhyYxtKVcaKpro")

ws = file.get_worksheet(0)

df = pd.DataFrame(ws.get_values())

print(df)


