#EXCEL EXTRACTION

from openpyxl import Workbook
workbook = Workbook()

sheet = workbook.active

def save_excel(invoice):
   sheet["A1"] = "VENDOR"
   sheet["B1"] = "INVOICE NUMBER"
   sheet["C1"] = "AMOUNT"
   sheet["D1"] = "GST"
   sheet["E1"] = "DATE"

# Append invoice details

   sheet.append([
      invoice["vendor"],
      invoice["invoice_number"],
      invoice["amount"],
      invoice["gst"],
      invoice["date"]
    ])



workbook.save("invoice_data.xlsx")

