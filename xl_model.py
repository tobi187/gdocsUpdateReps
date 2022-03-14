import dataclasses
import enum
import unicodedata


@dataclasses.dataclass
class ExcelModel:
    # All Rows from left to right in Excel starting at 1 (0), data starts at Col 10
    Unternehmen: str
    Geschaeftsfuehrer: str
    Telefon: str
    eMail: str
    Adresse: str
    Link: str  # Col 15
    Status: Status

    def to_upload_format(self) -> list[str]:
        return [
            self.Unternehmen,
            self.Geschaeftsfuehrer,
            self.Telefon,
            self.eMail,
            self.Adresse
        ]

    def email_part(self) -> str:
        mail = self.eMail.replace(".", "@")
        mail = mail.split("@")
        if len(mail) > 1:
            return mail[1]


@dataclasses.dataclass
class ExToCompare:
    eMail: str
    Unternehmen: str
    Telefon: str

    def to_unicode(self):
        self.eMail = unicodedata.normalize("NFKD", self.eMail)
        self.Unternehmen = unicodedata.normalize("NFKD", self.Unternehmen)
        self.Telefon = unicodedata.normalize("NFKD", self.Telefon)

    def strip(self):
        self.eMail = self.eMail.strip()
        self.Unternehmen = self.Unternehmen.strip()
        self.Telefon = self.Telefon.strip()


@dataclasses.dataclass
class GDocsModel:
    DocName: str
    WSName: str
    StartRow: str  # 10
    StartCol: str  # A
    EndCol: str  # E
    EndRow: str  # TODO: new Row (last entry + 1)

    def get_range(self, end_y) -> str:
        return f"{self.StartCol + self.start_row_update()}:{self.EndCol + str(end_y)}"

    def start_row_update(self) -> str:
        return str(int(self.EndRow) + 1)

    def link_range(self, length) -> str:
        start_index = self.start_row_update()
        end = start_index + length
        return f"O{start_index}:O{end}"


class Status(enum.Enum):
    Untested = 0,
    IsCopy = 1
    IsUnique = 2,
    NotSure = 3
