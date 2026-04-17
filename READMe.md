# 🇩🇰 Nordic Insurance AI

An end-to-end **AI-powered insurance risk prediction and pricing system** that combines Machine Learning with rule-based business logic to generate personalized insurance premiums.

---

## 🚀 Overview

This project predicts a user's insurance risk category (**Low / Medium / High**) using a trained ML model and calculates the final premium using Nordic-specific pricing rules such as:

- City-based risk factors  
- Smoking status  
- Income-based adjustment  
- Insurance tax factor  

It is designed as a **production-style system** with clear separation between ML, validation, and business logic.

---

## 🧠 System Architecture

Frontend (UI)
↓
FastAPI Backend
↓
Pydantic Validation
↓
ML Model (Risk Prediction)
↓
Pricing Engine (Business Rules)
↓
Final Output (Premium + Explanation)


---

## 🔄 End-to-End Flow

1. User enters details in the frontend  
2. Request is sent to FastAPI backend  
3. Pydantic validates the input  
4. ML model predicts risk category  
5. Pricing engine calculates premium  
6. Backend returns results  
7. Frontend displays insights  

---

## ⚙️ Features

- ✅ ML-based risk classification (Low / Medium / High)  
- ✅ Rule-based insurance pricing engine  
- ✅ City risk scoring (Denmark-focused 🇩🇰)  
- ✅ Smoking & income-based adjustments  
- ✅ Strict input validation using Pydantic  
- ✅ Explainable AI (clear pricing explanation)  
- ✅ Savings tips for users  
- ✅ Modular backend (production-ready structure)  

---

## 📦 Tech Stack

### 🔹 Backend
- Python
- FastAPI
- Pydantic

### 🔹 Machine Learning
- Scikit-learn
- Pandas
- Pickle

### 🔹 Frontend
- Streamlit / HTML / CSS / JavaScript

---

## 📊 Input Features

- Age (18–65)  
- Weight (55–100 kg)  
- Height (160–195 cm)  
- Annual Income (DKK 280k–800k)  
- Smoking Status  
- City (Denmark)  
- Occupation  

---

## 💰 Output

- Predicted Risk Category  
- Confidence Score  
- Class Probabilities  
- Final Insurance Premium (DKK)  
- Explanation of pricing  
- Personalized savings tips  

---

## 🧮 Pricing Logic

Final Premium = Base Premium × City Risk × Smoking Factor × Income Factor × Tax Factor

## 📁 Project Structure

NordicInsureAI/
│
├── backend/
│   ├── app.py                # FastAPI entry point
│   ├── predict.py           # ML inference logic
│   ├── config/              # Business rules & settings
│   │   ├── city_tiers.py
│   │   ├── nordic_adjustments.py
│   │   ├── pricing_service.py
│   │   └── settings.py
│   │
│   ├── model/               # Trained ML model (.pkl)
│   │   └── insurance_premium_predictor_model.pkl
│   │
│   ├── schema/              # Pydantic validation models
│   │   ├── user_input.py
│   │   └── prediction_response.py
│   │
│   └── utils/               # Helper functions
│       └── preprocess.py
│
├── frontend/
│   ├── assets/              # Images, logos
│   │   └── logo.png
│   └── streamlit_app.py    # UI application
│
├── data/                    # Dataset files
│   └── insurance_premium_dataset_sample.csv
│
├── notebooks/               # Experiments & training
│   ├── Dataset.py
│   └── ml_model_new.ipynb
│
├── artifacts/               # Generated outputs (reports/logs)
│
├── requirements.txt
└── README.md

---

## 🔄 System Workflow

User Input (Frontend)
↓
Streamlit UI
↓
FastAPI Backend (app.py)
↓
Pydantic Validation (schema/)
↓
ML Model Prediction (model/)
↓
predict.py (Inference Layer)
↓
Pricing Engine (config/)
↓
Final Response (Premium + Explanation)
↓
Frontend Display


---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---
## 🚀 Run the Project

### Start Backend (FastAPI)

```bash
uvicorn backend.app:app --reload
```

### Start Frontend (Streamlit)
```bash
streamlit run frontend/streamlit_app.py
```

## 📡 API Layer (FastAPI Service)

This project exposes a REST API built using **FastAPI** that allows external applications (frontend, apps, or other services) to access the ML model and pricing engine.

The API acts as the **bridge between the user interface and the AI system**, handling:

- Input validation (Pydantic)
- ML-based risk prediction
- Pricing engine execution
- Response formatting

---

## 📌 API Endpoint

### 🔹 Predict Insurance Premium

```text
POST /predict
```
---

## 📥 Example Request
{
  "age": 30,
  "weight": 75,
  "height": 180,
  "income_dkk": 500000,
  "smoker": false,
  "city": "Copenhagen",
  "occupation": "private_job"
}

---
## 📤 Example Response
{
  "predicted_category": "Medium",
  "confidence": 0.92,
  "final_premium_dkk": 8200,
  "currency": "DKK",
  "explanation": [
    "Base risk calculated from ML model",
    "City adjustment applied",
    "Smoking factor applied"
  ],
  "savings_tips": [
    "Avoid smoking to reduce premium",
    "Living in low-risk city reduces cost"
  ]
}
----

## 🧠 Key Features
ML-based risk prediction
Rule-based pricing engine
FastAPI backend
Streamlit frontend
Pydantic validation
Explainable AI outputs

---

## 📈 Future Improvements
Docker deployment
Cloud hosting (AWS / Azure)
Database integration
CI/CD pipeline
Model retraining automation

---
## 👩‍💻 Author

Parul Sharma  
AI/ML Engineer | Applied ML & DL 

## ⭐ Acknowledgement

If you found this project useful, consider starring the repository.