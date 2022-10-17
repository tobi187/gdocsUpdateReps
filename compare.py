from xl_model import ExcelModel, ExToCompare, Status, GDocsModel
import gspread

with open("providers.txt", "r") as file:
    black_list = file.readlines()


def by_email(old_data: list[ExToCompare], entry: ExcelModel):
    mail = entry.email_part()
    if mail == "" or mail in black_list:
        return entry
    if any(e.email_part() == mail for e in old_data):
        entry.Status = Status.IsCopy
        return entry
    entry.Status = Status.IsUnique


def by_company_name(old_data: list[ExToCompare], entry: ExcelModel):
    if any(e.Unternehmen.lower() == entry.Unternehmen.lower() for e in old_data):
        entry.Status = Status.IsCopy
        return entry
    else:
        entry.Status = Status.IsUnique
        return entry


                                                                # later only correct data
def compare(old_data: list[ExToCompare], new_data: list[ExcelModel]):

    data = [by_company_name(old_data, d) for d in new_data]

    correct_data = [d for d in data if d.Status == Status.IsUnique]
    copys = [d for d in data if d.Status == Status.IsCopy]

    return correct_data, copys


# def fill_data():
#     end = "A4400"
#     start = "A10"
#     gc = gspread.oauth()
#     wb = gc.open_by_key("1RPZ81nHBtbSvuNCE3gtCa4Fc-KRBelhyYxtKVcaKpro")
#     ws = wb.worksheet("Potentielle Kunden DE")
#
#     data: list[gspread.Cell] = ws.range(start + ":" + end)
#
#     for i, d in enumerate(data):
#         if d.value == "":
#             data[i].value = "PlaceHolder"
#
#     ws.update_cells(data)


