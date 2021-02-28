## Simple Machine Learning Model 

## Iniciar aplicación

1) Iniciar ambiente virtual 
        
        python3 -m venv env  
        source env/bin/activate   o  env\Scripts\activate 

2) Instalar dependencias

        pip install -r requirements.txt


3) Iniciar servidor local
        
        uvicorn app.main:app --reload



### APIs 
Se exponen 2 endpoints

/retrain : simula el rentrenamiento del modelo creando el archivo model.joblib

ejemplo local: http://localhost:8000/retrain

/predict/{sales}/{category} : los parámetros son pasados por medio de get 

ejemplo local : http://localhost:8000/predict/100/1





