<p align="center">
  <img src="assets/banner.png" alt="Nordic Insurance AI Banner" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Docker-Container-blue?logo=docker">
</p>

# 🇩🇰 Nordic Insurance AI

An end-to-end **machine learning-powered insurance pricing system** that predicts **customer risk** and calculates **dynamic insurance premiums** using **FastAPI**, **Streamlit**, and **Docker**.

---

## 🚀 Live Workflow

High-level flow of the system:

```text
Streamlit UI
        ↓
FastAPI /predict endpoint
        ↓
Pydantic validation
        ↓
Feature engineering / preprocessing
        ↓
ML risk prediction
        ↓
Pricing engine (business rules)
        ↓
Response returned to UI
```

---

## 🏗️ System Architecture

Detailed component-level architecture:

```mermaid
graph TD
A[Streamlit UI] --> B[FastAPI Backend]
B --> C[Pydantic Validation]
C --> D[Feature Engineering]
D --> E[ML Model Prediction]
E --> F[Pricing Engine]
F --> G[Response Builder]
G --> A
```
---

## ⚙️ Key Features

- Risk classification (Low / Medium / High)
- Dynamic premium calculation using business rules
- City-based risk scoring (Denmark 🇩🇰)
- Lifestyle-based adjustments (smoking, income)
- Input validation using Pydantic
- Explainable pricing decisions
- Personalized savings recommendations

---

## 🚀 Project Impact

This project demonstrates:

- End-to-end machine learning system design
- Production-style API-first architecture
- Dockerized microservices deployment
- Real-world insurance pricing engine
- Explainable AI for business transparency

---

## 🗂️ Dataset & Model

The system is built using an insurance dataset containing demographic, health, and lifestyle features.

### 📊 Dataset Features
- Age  
- Height
- Weight
- Income level  
- Smoking status  
- City/location  
- Occupation  

### ⚙️ Data Processing
- Data is cleaned and preprocessed  
- Categorical features are encoded  
- Numerical features are normalized  
- Feature engineering is performed to capture additional patterns and improve model performance  


### 🤖 Model Details

- **Model Type:** Gradient Boosting Classifier  
- **Task:** Multi-class classification (Low / Medium / High risk)  
- **Output:** Risk category with confidence score  

---

## 🔄 System Overview

1. User enters details in Streamlit UI  
2. Request is sent to FastAPI backend  
3. Pydantic validates input data  
4. Features are engineered/preprocessed  
5. ML model predicts risk category  
6. Pricing engine calculates insurance premium  
7. Response is formatted and returned  
8. Streamlit displays results  

---

## 🧠 Explainability

The system provides transparent insurance decisions by breaking down how the final risk and premium are calculated.

### 🔍 Key Factors

- **ML Model Output** – Base risk predicted from user data  
- **City Adjustment** – Location-based risk variation  
- **Smoking Factor** – Increased risk for smokers  
- **Income Impact** – Normalization for fair pricing  

### ✅ Outcome
- Transparent  
- Interpretable  
- User-friendly

---

## 📦 Tech Stack

### 🖥️ Backend
- Python  
- FastAPI  
- Pydantic  

### 🤖 Machine Learning
- Scikit-learn  
- Pandas  
- Pickle  

### 🌐 Frontend
- Streamlit  

### 🐳 DevOps
- Docker
- Docker Compose

---

## 📊 Input & Output Overview

### 🧾 Input Features

- Age (18–65 years)
- Weight (55–100 kg)
- Height (160–195 cm) 
- Annual Income (DKK 280k–800k)  
- Smoking Status  
- City (Denmark)  
- Occupation  

### 🎯 Model Output
- Risk Category (Low / Medium / High)  
- Confidence Score  
- Final Insurance Premium (DKK)  
- Explanation of pricing factors  
- Personalized savings tips

  ---

## 🧮 Pricing Logic

The final insurance premium is calculated using a rule-based pricing engine that adjusts risk based on multiple factors.

### 💰 Formula

\[
Final\ Premium = Base\ Premium \times City\ Risk \times Smoking\ Factor \times Income\ Factor \times Tax\ Factor
\]

### ⚙️ Key Adjustments

- **City Risk** – Location-based risk multiplier (Denmark regions 🇩🇰)  
- **Smoking Factor** – Higher premium for smokers  
- **Income Factor** – Adjusts affordability and risk level  
- **Tax Factor** – Regional insurance tax adjustment  

---

## 📁 Project Structure

```text
NordicInsureAI/
│
├── README.md
├── docker-compose.yml
├── requirements.txt
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   ├── predict.py
│   │
│   ├── config/
│   │   ├── nordic_adjustments.py
│   │   ├── pricing_service.py
│   │   └── settings.py
│   │
│   ├── model/
│   │   └── insurance_premium_predictor_model.pkl
│   │
│   ├── schema/
│   │   ├── user_input.py
│   │   └── prediction_response.py
│   │
│   └── utils/
│       └── preprocess.py
│
├── frontend/
│   ├── Dockerfile
│   ├── streamlit_app.py
│   └── assets/
│       └── logo.png
│
├── shared/
│   └── config/
│       └── city_tiers.py
│
├── data/
│   └── insurance_premium_dataset_sample.csv
│
├── notebooks/
│   └── ml_model_new.ipynb
│
├── artifacts/
│   └── insurance_report.pdf
```

---

## 📡 FastAPI Layer

The backend exposes a REST API that handles:

- Input validation
- ML prediction
- Pricing calculation
- Response formatting

### 📥 Example Request (FastAPI)

```json
{
  "age": 37,
  "weight": 59,
  "height": 180,
  "income_dkk": 460000,
  "smoker": true,
  "city": "Esbjerg",
  "occupation": "freelancer"
}
```

### 📤 Example Response

```json
{
  "predicted_category": "Medium",
  "confidence": 0.92,
  "final_premium_dkk": 8200,
  "currency": "DKK",
  "explanation": [
     "Your insurance starts from a base price of 600 DKK based on your risk category (Medium)",
     "Living in Esbjerg has a neutral impact on your risk score (multiplier: 1.0)",
     "Smoking increases health risk and therefore your premium",
     "Your income level (DKK 460000.0) adjusts affordability (multiplier: 1.0)",
     " A standard Danish insurance tax is applied to the final premium"
  ],
  "savings_tips": [
    "Avoid smoking to reduce premium",
    "Living in low-risk city reduces cost"
  ]
}
```
---

## 🖥️ Streamlit Application

Interactive frontend for the insurance risk and pricing system.

### ⚙️ Features
- User input form (age, income, city, lifestyle)
- Sends request to FastAPI `/predict`
- Displays:
  - Risk category
  - Confidence score
  - Final premium (DKK)
  - Explanation of factors
  - Savings tips

### 📊 Visualization
- Waterfall chart showing:
  - Base ML risk
  - City adjustment
  - Smoking factor
  - Income adjustment

### 📄 PDF Report
  - Downloadable text-only report
  - Includes risk, premium, explanation, and tips  
  - Sample: `artifacts/insurance_report.pdf`

  ---
  
## 🚀  Run with Docker

```bash
docker-compose up --build
```
### 🌐 Access Application
| Service         | URL                                                      |
|----------------|----------------------------------------------------------|
| 🎨 **Streamlit UI** | [http://localhost:8501](http://localhost:8501)           |
| ⚙️ **FastAPI Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) |

---

## 🎯 Design Principles

- Separation of concerns  
- Modular architecture  
- Explainable AI (XAI)  
- Scalable backend design  
- Business-rule driven pricing
  
---

## 📈 Future Improvements

- Cloud deployment (AWS / Azure / GCP)
- CI/CD pipeline (GitHub Actions)
- Model retraining automation
- Database integration (PostgreSQL / MongoDB)

---

## 👩‍💻 Author

**Parul Sharma** 

AI/ML Engineer | Applied ML & DL 

## ⭐ Acknowledgement

If you found this project useful, consider starring the repository.
