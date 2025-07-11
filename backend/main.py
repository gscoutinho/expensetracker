# main.py
from fastapi import FastAPI
from api.user_router import router as user_router
from api.category_router import router as category_router
from api.transaction_router import router as transaction_router

app = FastAPI(title="Expense Tracker API")

app.include_router(user_router)
app.include_router(category_router)
app.include_router(transaction_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API"}