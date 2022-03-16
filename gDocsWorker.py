import xl_model
import pandas as pd
import gspread
from xl_model import ExToCompare, GDocsModel

gc = gspread.oauth()


def get_data() -> tuple[list[ExToCompare], GDocsModel]:
    doc = xl_model.GDocsModel(
        DocName="1RPZ81nHBtbSvuNCE3gtCa4Fc-KRBelhyYxtKVcaKpro",
        WSName="Potentielle Kunden DE",
        StartRow="9",
        StartCol="A",
        EndRow="",
        EndCol="E"
    )

    file = gc.open_by_key(doc.DocName)
    ws = file.worksheet(doc.WSName)
    df = pd.DataFrame(ws.get_values())
    important_data = []
    end_index = 9
                                # unternehmen, telefon, email
    for index, row in enumerate(df[[0, 2, 3]].to_numpy()[int(doc.StartRow):]):
        if row[0] == "":
            end_index += index
            doc.EndRow = str(end_index + 1)
            break

        important_data.append(xl_model.ExToCompare(
            Unternehmen=row[0],
            Telefon=row[1],
            eMail=row[2]
        ))

    return important_data, doc


def update_gdocs(data: list[xl_model.ExcelModel], doc: xl_model.GDocsModel):
    data_correct = [d.to_upload_format() for d in data]

    file = gc.open_by_key(doc.DocName)
    ws = file.worksheet(doc.WSName)
    ws.update(doc.get_range(len(data_correct)), data_correct)

    # update links
    links = [d.Link for d in data]
    link_cells: list[gspread.Cell] = ws.range(doc.link_range(len(links)))

    for index, entry in enumerate(links):
        link_cells[index].value = entry

    ws.update_cells(link_cells)


def backup_service():
    file = gc.open_by_key("1RPZ81nHBtbSvuNCE3gtCa4Fc-KRBelhyYxtKVcaKpro")
    sheet_names: list[gspread.Worksheet] = file.worksheets()
    titles = [t.title for t in sheet_names]
    if "Potentielle Kunden DE Backup" in titles:
        backup_ws = file.worksheet("Potentielle Kunden DE Backup")
        file.del_worksheet(backup_ws)
    ws = file.worksheet("Potentielle Kunden DE")
    ws.duplicate(new_sheet_name="Potentielle Kunden DE Backup", insert_sheet_index=len(titles))

