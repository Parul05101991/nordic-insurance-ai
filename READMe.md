<p align="center">
  <img src="frontend/assets/banner.png" alt="Nordic Insurance AI Banner" width="100%"/>
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

## 🎯 Quick Highlights

- End-to-end ML system (UI + API + Model)
- Real-world insurance pricing simulation
- Fully Dockerized deployment
- Explainable AI for transparent decisions

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

## 📌 Why This Project Matters

This project demonstrates a production-style ML system by integrating:

- ML-based risk scoring  
- Rule-based pricing engine  
- API-first backend architecture  
- Containerized deployment with Docker

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

## 🧠 Explainability & Pricing Logic

The system provides transparent insurance decisions by combining machine learning predictions with rule-based adjustments. Each factor contributes to the final premium in a clear and interpretable way.

### 💰 Formula

`Final Premium = Base Premium × City Risk × Smoking Factor × Income Factor × Tax Factor`

### 🔍 Key Factors

- **ML Model Output** – Base risk predicted from user data  
- **City Risk** – Location-based risk multiplier  
- **Smoking Factor** – Higher premium for smokers  
- **Income Factor** – Adjusts affordability and risk level  
- **Tax Factor** – Standard regional insurance tax  

### ✅ Outcome
- Transparent decision-making  
- Interpretable pricing  
- User-friendly explanations
  
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

## 📡 FastAPI Layer

The backend exposes a REST API for:
- Input validation  
- ML risk prediction  
- Premium calculation  

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
  "final_premium_dkk": 8200
}
```

🔗 Full API documentation available at `/docs`  
(Accessible at http://localhost:8000/docs when running locally)

---

## 🖥️ Streamlit Application

Interactive frontend for user input and real-time premium calculation.

### ⚙️ Features
- Input form (age, income, city, lifestyle)
- Calls FastAPI `/predict` endpoint
- Displays risk category, confidence, and final premium

### 📊 Visualization
- Waterfall chart showing contribution of pricing factors

### 📄 Report
- Downloadable PDF with risk, premium, and explanation  
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
