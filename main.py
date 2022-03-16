import gDocsWorker
import excelWorker
import compare


def main():
    gDocsWorker.backup_service()
    google_data, doc = gDocsWorker.get_data()

    # TODO: get Excel Data
    excel_data = excelWorker.get_data(r"C:\Users\fisch\Desktop\projects\efly\scrape\lead_neu (31).xlsx")
    # TODO: compare data remove duplicates

    save_data, copy = compare.compare(google_data, excel_data)

    gDocsWorker.update_gdocs(save_data, doc)


if __name__ == "__main__":
    main()
