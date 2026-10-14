# 🤖 AI Invoice Automation System

An AI-powered backend application that automates invoice processing using FastAPI and Google Gemini AI.

The system accepts PDF invoices, extracts invoice information using AI, converts it into structured JSON, and exports the data into an Excel spreadsheet automatically.

---

## 🚀 Features

- Upload PDF invoices
- Extract invoice text
- AI-based invoice information extraction
- Structured JSON output
- Automatic Excel generation
- FastAPI REST API
- Modular project architecture

---

## 🛠 Tech Stack

- Python
- FastAPI
- Google Gemini API
- PyPDF
- OpenPyXL
- JSON
- Uvicorn
- Python Dotenv

---

## 📂 Project Structure

```
ai_invoice_automation/
│
├── app/
│   ├── router/
│   ├── services/
│   ├── config.py
│
├── uploads/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Workflow

```
PDF Upload
      ↓
Extract Text
      ↓
Gemini AI
      ↓
JSON Output
      ↓
Excel Generation
```

---

## API Endpoint

### Upload Invoice

```
POST /upload
```

Upload a PDF invoice and receive structured invoice information.

---

## Example JSON Response

```json
{
    "uploaded": "File Invoice Uploaded Successfully",
    "vendor": "ABC Pvt Ltd",
    "invoice_number": "INV-001",
    "amount": "25000",
    "gst": "4500",
    "date": "2026-10-14"
}
```

---

## Future Improvements (V2)

- Multiple PDF Upload
- Batch Invoice Processing
- Better Error Handling
- Retry Logic
- Deployment
- Modern Frontend Dashboard

---

## Author

**Mudit Joshi**

AI Automation Learning Journey 🚀
