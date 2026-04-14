from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel, Field
import joblib
pipeline = joblib.load("pipeline.pkl")
class Input(BaseModel):
    category: str = Field(..., example='misc',description='Category of the transaction grocery home shopping' 'travel' 'misc''entertainment' 'personal' 'health')
    amt: float = Field(..., example=49.14,description='Amount of the transaction')
    gender: str = Field(..., example='M',description='Gender of the user M or F')
    age: int = Field(..., example=53,description='Age of the user')
    day: str = Field(..., example='Tue',description='Day of the transaction Mon Tue Wed Thu Fri Sat Sun')
    hour: int = Field(..., example=23,description='Hour of the transaction in 24-hour format')
    distance_km: str = Field(..., example='Local',description='Distance of the transaction in km Local 0-20, Commute 20-60, Regional 60-80, Long_Distance 80-120 Remote 120-')



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Credit-Card-Fraud-Detection API"}


@app.post("/predict")
async def predict(input: Input):
    sample_data = [[input.category, input.amt, input.gender, input.age, input.day, input.hour, input.distance_km]]
    sample_df = pd.DataFrame(sample_data, columns=['category', 'amt', 'gender', 'age', 'day', 'hour', 'distance_km'])
    prediction = pipeline.predict(sample_df)
    result = int(prediction[0])
    return {"prediction": result,"is_fraud": True if result == 1 else False}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


