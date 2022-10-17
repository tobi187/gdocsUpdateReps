import gDocsWorker
import excelWorker
import compare


def main():
    #gDocsWorker.backup_service()
    #google_data, doc = gDocsWorker.get_data()

    # TODO: get Excel Data
    excel_data = excelWorker.get_data(r"C:\Users\fisch\Desktop\excel combine test\USA_Leads4.xlsx")
    # TODO: compare data remove duplicates

    return
    save_data, copy = compare.compare(google_data, excel_data)

    gDocsWorker.update_gdocs(save_data, doc)


if __name__ == "__main__":
    main()
