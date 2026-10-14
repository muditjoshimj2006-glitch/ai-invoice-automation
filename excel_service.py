#EXCEL EXTRACTION
from openpyxl import load_workbook
import os
from openpyxl import Workbook

if os.path.exists("invoice_data.xlsx"):
    workbook = load_workbook("invoice_data.xlsx")
    sheet = workbook.active
else:
    workbook = Workbook()
    sheet = workbook.active


def save_excel(invoice):

    if sheet.max_row == 1 and sheet["A1"].value is None:
        sheet["A1"] = "VENDOR"
        sheet["B1"] = "INVOICE NUMBER"
        sheet["C1"] = "AMOUNT"
        sheet["D1"] = "GST"
        sheet["E1"] = "DATE"

    # Duplicate Check
    for row in sheet.iter_rows(min_row=2):

        if (
            invoice["invoice_number"] != "" and
            row[1].value == invoice["invoice_number"]
        ):
            print("Invoice Already Exists")
            return

    # Append invoice
    sheet.append([
        invoice["vendor"],
        invoice["invoice_number"],
        invoice["amount"],
        invoice["gst"],
        invoice["date"]
    ])

    workbook.save("invoice.xlsx")