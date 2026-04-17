# Main FastAPI API
import pandas as pd
from fastapi import FastAPI, HTTPException
from backend.schema.user_input import UserInput
from backend.schema.prediction_response import PredictionResponse
from backend.predict import predict_output, MODEL_VERSION, model
from backend.utils.preprocess import build_features
from backend.config.pricing_service import calculate_final_premium


app = FastAPI(
    title="NordicInsure AI",
    description="Denmark Insurance Premium Prediction System 🇩🇰",
    version="1.0.0"
)


# human readable
@app.get("/")
def home():
     return {"message": "NordicInsure AI is running 🚀"}


# machine readable
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)

def predict_premium(data: UserInput):

    try:
        
        # 1. Feature Engineering
        
        features = build_features(data)
        model_input = pd.DataFrame([features])

        
        # 2. ML Prediction
        
        probs = model.predict_proba(model_input)[0]
        classes = model.classes_

        prob_dict = {str(k): float(v) for k, v in zip(classes, probs)}

        predicted_category = max(prob_dict, key=prob_dict.get)
        confidence = max(probs)

        
        # 3. Business Logic (Pricing)
        
        pricing = calculate_final_premium(predicted_category,data.city,data.smoker,data.income_dkk)

        
        # 4. Response
        
        return {
            "predicted_category": predicted_category,
            "confidence": float(confidence),
            "class_probabilities": prob_dict,
            **pricing   #  include business logic output
        }

    except Exception as e:
        if model is None:
           raise HTTPException(status_code=500, detail="Model not loaded")
        