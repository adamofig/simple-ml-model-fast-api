import math
import random

import joblib
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.model import Model

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_default_html_docs():
    """Método raíz devuelve texto en html"""

    return f"""
    <h4> Machine Learning Model Demo </h4>
    <li> <a href="/docs"> Ver Documentación </a>  </li>
    <li> <a href="/predict/100/100"> ejemplo consulta </a>  </li>
    """

@app.get("/predict/{sales}/{category}")
def model_data(sales : float, category: float):
    try:
        model = joblib.load("./model.joblib")
        result = model.predict(sales, float(category))
    except:
        return {"results": "The model can't be loaded try /retrain"}
    return {"resultados":result}


@app.get("/retrain")
def retrain_model():
    try:
        print("Rentrenando Modelo")
        model = Model()
        joblib.dump(model, "./model.joblib")
    except Exception as e:
        print("Can't save model")
    return {"results" : "The model was retraining and successfully saved"}







