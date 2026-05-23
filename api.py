from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")

class UserInput(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    educational_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

@app.get("/")
def home():
    return {"message": "Adult Income Prediction API"}

@app.post("/predict")
def predict(data: UserInput):

    input_data = pd.DataFrame([{
        "age": data.age,
        "workclass": data.workclass,
        "fnlwgt": data.fnlwgt,
        "education": data.education,
        "educational-num": data.educational_num,
        "marital-status": data.marital_status,
        "occupation": data.occupation,
        "relationship": data.relationship,
        "race": data.race,
        "gender": data.gender,
        "capital-gain": data.capital_gain,
        "capital-loss": data.capital_loss,
        "hours-per-week": data.hours_per_week,
        "native-country": data.native_country
    }])

    prediction = model.predict(input_data)[0]

    return {"prediction": prediction}