from fastapi import FastAPI
from app.router.invoice import router

app = FastAPI(debug=True)
app.include_router(router)

@app.get("/")
def home():
    return{
        "message" : "Welcome To The AI Invoice Automation System"
    }

