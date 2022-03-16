import pandas as pd
from xl_model import ExcelModel, Status


def convert_row(bus_name, bus_info, link) -> ExcelModel:
    company_name = bus_name.split("\n")[0]
    info = {"Business Name:": "", "Number:": "", "Business Address:": ""}
    col_names = ["Business Name:", "Type:", "RegNum:", "Number:", "Business Address:", "Representative Name:", "VAT Number:", "number:", "Customer Services Address:"]
    bus_info = bus_info.replace("Register Number", "RegNum")
    bus_info = bus_info.replace("Detailed Seller Information\n", "")
    for name in col_names:
        bus_info = bus_info.replace(name, ";" + name + ";")
    bus_info = bus_info.split(";")
    bus_info = [d for d in bus_info if d != ""]
    for index, entry in enumerate(bus_info):
        if entry in info.keys():
            info[entry] = bus_info[index + 1]

    return ExcelModel(
        Unternehmen=company_name.strip(),
        Geschaeftsfuehrer=info["Business Name:"],
        Telefon=info["Number:"].replace("DE", "+49 "),
        Adresse=info["Business Address:"],
        eMail="",
        Link=link.strip(),
        Status=Status.Untested
    )


def get_data(path: str) -> list[ExcelModel]:
    excel_data = pd.read_excel(path, sheet_name="Sheet1")
    needed_colnames = ["Händler-Info1", "Händler-Info2", "Land", "Schaufenster-link-href"]
    clean_data = []
    for entry in excel_data[needed_colnames].to_numpy():
        if entry[1] == "":
            continue
        if str(entry[2]).strip() != "DE":
            continue

        c_row = convert_row(entry[0], entry[1], entry[3])
        clean_data.append(c_row)

    return clean_data
