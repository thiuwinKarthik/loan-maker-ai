from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Loan AI Microservice")

class LoanRequest(BaseModel):
    age: int
    income: float
    existing_emi: float
    credit_score: int
    asset_value: float
    loan_amount: float
    tenure: int

# Load trained model
with open("services/loan_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(request: LoanRequest):
    data = request.dict()
    # Convert to model input format
    X = np.array([[data["age"], data["income"], data["existing_emi"],
                   data["credit_score"], data["asset_value"],
                   data["loan_amount"], data["tenure"]]])
    prediction = model.predict(X)[0]  # 0 or 1
    return {"approved": bool(prediction)}

# Existing recommend endpoint
from services.loan_recommendation import recommend_lenders

@app.post("/recommend")
def recommend(request: LoanRequest):
    user_data = request.dict()
    lenders = recommend_lenders(user_data)
    return {"recommendations": lenders}
