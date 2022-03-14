import gDocsWorker
import xl_model
import excelWorker


def main():
    gDocsWorker.backup_service()
    google_data, doc = gDocsWorker.get_data()

    # TODO: get Excel Data
    # TODO: compare data remove duplicates

    gDocsWorker.update_gdocs([], doc)