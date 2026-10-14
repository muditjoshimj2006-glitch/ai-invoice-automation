from google import genai
from app.config import api_key

def ai_analysis(text):
    try:
       client = genai.Client(api_key=api_key)

       prompt = f"""
Extract the invoice details from the text below.

{text}

Return ONLY a valid JSON object.

Do NOT use markdown.
Do NOT write ```json.
Do NOT write any explanation.

Return exactly:

{{
  "vendor": "",
  "invoice_number": "",
  "amount": "",
  "gst": "",
  "date": ""
}}
"""

       response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


       return response.text


    except Exception as e:
        print(f"AI CALLING FAILED : {e}")
        raise

