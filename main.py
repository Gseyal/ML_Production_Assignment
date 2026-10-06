
import pickle
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel,Field
import pandas as pd
from pathlib import Path
from fastapi.responses import FileResponse
app=FastAPI()
with open('model.pkl','rb') as file: # opened model.pkl as read binary
    model=pickle.load(file)

class IrisInput(BaseModel):
    sepal_length:  float = Field(gt=0) # variable: expected_type=Field(gt-> greater than)
    sepal_width:  float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width:  float = Field(gt=0)


@app.get("/")
def home():
    return FileResponse(Path(__file__).parent / "pages/index.html")

@app.get("/health")
def health():
    return {"message": "Iris API is running."}

@app.post("/predict")
def predict(data: IrisInput):
    values=[[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    header=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
    inputs=pd.DataFrame(values,columns=header)

    prediction = model.predict(inputs)[0]
    return {"prediction": str(prediction)}