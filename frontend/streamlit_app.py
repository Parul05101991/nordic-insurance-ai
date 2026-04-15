import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import json
import sys
import os
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import uuid


# REPORT META

report_id = str(uuid.uuid4())[:8].upper()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# PATH SETUP

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.config.city_tiers import tier_1_cities, tier_2_cities


# PAGE CONFIG

st.set_page_config(page_title="NordicInsure AI", layout="centered")

st.title("🇩🇰 NordicInsure AI - Smart Insurance Engine")
st.markdown("---")


# INPUTS

st.subheader("🧾 Personal Details")
full_name = st.text_input("Full Name", placeholder="Enter your full name")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 65, 30)
    weight = st.number_input("Weight (kg)", 55.0, 100.0, 60.0)
    height = st.number_input("Height (cm)", 160.0, 195.0, 175.0)

with col2:
    income_dkk = st.slider("Annual Income (DKK)", 280000, 800000, 550000, step=20000)
    smoker = st.toggle("Do you smoke? ")
    occupation = st.selectbox(
        "Occupation",
        ["retired", "freelancer", "student",
         "government_job", "business_owner",
         "unemployed", "private_job"]
    )

bmi = weight / ((height / 100) ** 2)
st.info(f" Your BMI: {bmi:.1f}")


# CITY

st.subheader("📍 Location")
all_cities = sorted(list(set(tier_1_cities + tier_2_cities)))
city = st.selectbox("City", all_cities)


# SIDEBAR

st.sidebar.title("⚙️ Controls")

compare_mode = st.sidebar.checkbox("🔄 Compare Mode")

if compare_mode:
    st.sidebar.success("🔍 Active: Comparing Smoker vs Non-Smoker scenario")
    st.sidebar.markdown("""
    <div style="background-color:#1f2937; padding:12px; border-radius:10px;">
    <h4 style="color:#60a5fa;">📊 Compare Mode</h4>
    <p style="color:white;">We compare two insurance scenarios:</p>
    <p style="color:#fbbf24;">🚬 Scenario 1: You continue smoking</p>
    <p style="color:#34d399;">🚭 Scenario 2: You do NOT smoke</p>
    <hr style="border:0.5px solid #374151;">
    <p style="color:#f87171; font-weight:bold;">💡 Result:</p>
    <p style="color:white;">We show how much money you save if you quit smoking.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.info("Turn ON Compare Mode to simulate smoking impact.")

submit = st.button("🚀 Generate Insurance Report")


# API CALL

def get_prediction(smoker_status: bool):
    url = "http://127.0.0.1:8000/predict"

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_dkk": income_dkk,
        "smoker": smoker_status,
        "city": city,
        "country": "Denmark",
        "occupation": occupation
    }

    try:
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code != 200:
            st.error(res.text)
            return None
        return res.json()
    except Exception as e:
        st.error(f"API Error: {e}")
        return None


# GAUGE

def show_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': "Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))
    return fig


# WATERFALL

def show_waterfall(result):
    base = result["base_premium"]

    step1 = base * result["city_multiplier"]
    step2 = step1 * result["smoker_multiplier"]
    step3 = step2 * result["income_multiplier"]
    step4 = step3 * result["tax_factor"]

    fig = go.Figure(go.Waterfall(
        measure=["absolute", "relative", "relative", "relative", "relative", "total"],
        x=["Base", "City", "Smoker", "Income", "Tax", "Final"],
        y=[base, step1-base, step2-step1, step3-step2, step4-step3, step4]
    ))
    return fig


# PDF FUNCTION (FIXED)

def create_pdf(result, report_id, timestamp):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    width, height = letter
    y = 750

    # =========================
    # 🏢 HEADER WITH LOGO
    # =========================
    try:
        logo_path = "/Users/parulsharma/Desktop/NordicInsureAI /frontend/assets/logo.png"
        c.drawImage(logo_path, 50, y-20, width=60, height=40)
    except:
        pass

    c.setFont("Helvetica-Bold", 19)
    c.setFillColorRGB(0.12, 0.30, 0.47)  # navy tone
    c.drawString(120, y, "NordicInsure AI")

    y -= 20
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.drawString(120, y, "Smart Insurance Risk & Pricing Report")

    # Divider
    y -= 15
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    c.line(50, y, 550, y)

    y -= 30

    # =========================
    # 📌 META INFO
    # =========================
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0, 0, 0)

    c.drawString(50, y, f"Report ID:")
    c.drawString(150, y, report_id)

    y -= 15
    c.drawString(50, y, f"Generated at:")
    c.drawString(150, y, timestamp)

    y -= 30

    # =========================
    # 👤 CUSTOMER DETAILS BOX
    # =========================
    c.setFillColorRGB(0.95, 0.97, 1)  # light blue background
    c.rect(50, y-40, 500, 50, fill=1, stroke=0)

    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(60, y, "Customer Details")

    c.setFont("Helvetica", 10)
    c.drawString(60, y-20, f"Name: {full_name if full_name.strip() else 'N/A'}")
    c.drawString(300, y-20, f"City: {city}")

    y -= 70

    # =========================
    # 💰 SUMMARY BOX (HIGHLIGHT)
    # =========================
    c.setFillColorRGB(0.92, 0.97, 0.92)  # light green
    c.rect(50, y-60, 500, 70, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(0, 0.4, 0)
    c.drawString(60, y, "Insurance Summary")

    c.setFont("Helvetica", 11)
    c.setFillColorRGB(0, 0, 0)

    c.drawString(60, y-20, f"Final Premium: {result['final_premium']} DKK")
    c.drawString(60, y-35, f"Risk Category: {result['predicted_category']}")
    c.drawString(300, y-20, f"Confidence: {result['confidence']*100:.2f}%")

    y -= 90

    # =========================
    # 📊 USER INPUT DETAILS
    # =========================
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "User Profile")

    y -= 20
    c.setFont("Helvetica", 10)

    c.drawString(50, y, f"Age: {age}")
    c.drawString(150, y, f"BMI: {round(bmi,2)}")
    c.drawString(300, y, f"Income: {income_dkk} DKK")

    y -= 15
    c.drawString(50, y, f"Occupation: {occupation}")
    c.drawString(300, y, f"Smoker: {'Yes' if smoker else 'No'}")

    y -= 30

    # =========================
    # 🧠 EXPLANATION SECTION
    # =========================
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Risk Explanation")

    y -= 20
    c.setFont("Helvetica", 9)

    for item in result.get("explanation", []):
        if y < 80:
            c.showPage()
            y = 750

        lines = [item[i:i+90] for i in range(0, len(item), 90)]
        for line in lines:
            c.drawString(50, y, f"- {line}")
            y -= 12
        y -= 5

    # =========================
    # ⚠️ FOOTER
    # =========================
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(0.5, 0.5, 0.5)

    c.drawString(50, 40, "This report is generated by NordicInsure AI")
    c.drawRightString(550, 40, f"Report ID: {report_id}")

    # =========================
    # SAVE
    # =========================
    c.save()
    buffer.seek(0)

    return buffer.getvalue()


# VALIDATION

if submit and not full_name.strip():
    st.error("⚠️ Full Name is required")
    st.stop()


# MAIN

if submit:

    result = get_prediction(smoker)

    if result is None:
        st.stop()

    st.success("✅ Prediction Complete")

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Premium", result["final_premium"])
    col2.metric("📊 Risk", result["predicted_category"])
    col3.metric("🎯 Confidence", f"{result['confidence']*100:.2f}%")

    st.plotly_chart(show_gauge(
        {"Low": 25, "Medium": 60, "High": 90}.get(result["predicted_category"], 25)
    ))

    
    # COMPARISON
    
    if compare_mode and smoker:

        st.markdown("## 🔄 Smoking Impact Analysis")

        res_non_smoker = get_prediction(False)

        if res_non_smoker:
            col1, col2 = st.columns(2)

            col1.metric("🚬 Smoker", result["final_premium"])
            col2.metric("🚭 Non-Smoker", res_non_smoker["final_premium"])

            savings = result["final_premium"] - res_non_smoker["final_premium"]
            st.success(f"💰 You save {savings:.2f} DKK/year")

            fig = px.bar(
                x=["Smoker", "Non-Smoker"],
                y=[result["final_premium"], res_non_smoker["final_premium"]],
                title="Smoking Impact"
            )
            st.plotly_chart(fig)

    
    # WATERFALL
    
    st.markdown("## 📊 Premium Breakdown")
    st.plotly_chart(show_waterfall(result))

    
    # PDF DOWNLOAD
    
    pdf_file = create_pdf(result, report_id, timestamp)

    st.download_button(
        "📄 Download PDF",
        pdf_file,
        file_name="insurance_report.pdf",
        mime="application/pdf"
    )

    
    # JSON DOWNLOAD
    
    st.download_button(
        "📥 Download JSON",
        json.dumps(result, indent=2),
        file_name="insurance_report.json",
        mime="application/json"
    )