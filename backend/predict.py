import pickle
import pandas as pd
from backend.config.settings import MODEL_PATH
from backend.config.pricing_service import calculate_final_premium
from backend.schema.user_input import UserInput


# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"
class_labels = model.classes_.tolist()

# MAIN ML PREDICTION FUNCTION


def predict_output(user_input: UserInput):

    # Convert input to DataFrame
    df = pd.DataFrame([user_input.model_dump()])

  
    # ML Prediction
    
    predicted_class = model.predict(df)[0]

    probabilities = model.predict_proba(df)[0]

    confidence = float(max(probabilities))

    class_probs = dict(
        zip(class_labels, map(lambda p: round(float(p), 4), probabilities))
    )


    # CALL YOUR PRICING ENGINE
    
    pricing_result = calculate_final_premium(
        predicted_category=predicted_class,
        city=user_input.city,
        smoker=user_input.smoker,
        income_dkk=user_input.income_dkk
    )

    # ----------------------------
    # FINAL RESPONSE
    # ----------------------------
    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,

        # from pricing engine
        "pricing": pricing_result,

        # quick access fields (optional for frontend)
        "final_premium_dkk": pricing_result["final_premium"],
        "currency": pricing_result["currency"],
        "explanation": pricing_result["explanation"],
        "savings_tips": pricing_result["savings_tips"]
    }