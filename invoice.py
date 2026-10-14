#UPLOAD INVOICE

from fastapi import UploadFile, File
from fastapi import APIRouter
from app.services.ai_service import ai_analysis
from app.services.pdf_service import read_pdf
from app.services.excel_service import save_excel
from typing import List
import os
import shutil
import json

router = APIRouter()



@router.post("/upload")
async def upload_invoice(file: UploadFile = File(...)):

        os.makedirs("uploads",exist_ok=True)
 
        file_path = os.path.join("uploads",file.filename)

        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file ,buffer)
            print("File Saved Successfully")



        #pdf reading
        text = read_pdf(file_path)
        print("PDF Read Successfully")

        # ai analysis
        analysis = ai_analysis(text)

        #json
        analysis_data = json.loads(analysis)

        #excel saving
        save_excel(analysis_data)
        print("Excel Saved")


        return{
          "uploaded" : "File Invoice Uploaded Successfully",
          "vendor" : analysis_data["vendor"],
          "invoice_number" : analysis_data["invoice_number"],
          "amount" : analysis_data["amount"],
          "gst" : analysis_data["gst"],
          "date" : analysis_data["date"]

    }

