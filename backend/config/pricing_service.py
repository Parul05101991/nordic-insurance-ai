# Denmark Insurance Pricing Engine
#(ML + Business Rules + Explainability + Safety)

from shared.config.city_tiers import tier_1_cities, tier_2_cities
from backend.config.nordic_adjustments import (
    SMOKER_MULTIPLIER,
    TAX_FACTOR,
    CITY_RISK_SCORE,
    BASE_PREMIUM
)


# Preprocess city lists 
tier_1 = [c.lower() for c in tier_1_cities]
tier_2 = [c.lower() for c in tier_2_cities]



# Income logic (DKK)
def get_income_multiplier(income_dkk: float):
    if income_dkk < 350000:
        return 1.2
    elif income_dkk < 750000:
        return 1.0
    else:
        return 0.9



# City risk logic (SAFE + CONSISTENT)

def get_city_multiplier(city: str) -> float:
    if not city:
        return 1.0

    city = city.strip().title()

    return CITY_RISK_SCORE.get(city, 1.0)



# Main pricing engine

def calculate_final_premium(
    predicted_category: str,
    city: str,
    smoker,
    income_dkk: float
):

    
    # SAFE smoker handling
    
    if isinstance(smoker, str):
        smoker = smoker.strip().lower() in ["yes", "true", "1"]

    
    # Base premium from ML model
    
    base = BASE_PREMIUM.get(predicted_category, 500)

    
    # Risk multipliers
    
    city_mult = get_city_multiplier(city)
    smoker_mult = SMOKER_MULTIPLIER if smoker else 1.0
    income_mult = get_income_multiplier(income_dkk)

    
    # Final premium calculation
    
    final = base * city_mult * smoker_mult * income_mult * TAX_FACTOR

    
    # Safe city display (avoid crash)
    
    city_display = str(city).strip().title() if city else "Unknown"

    
    # User-friendly explanation
    
    explanation = [
        f"Your insurance starts from a base price of {base} DKK based on your risk category ({predicted_category}).",
        f"Living in {city_display} affects your risk score (multiplier: {city_mult}).",
        "Smoking increases health risk and therefore your premium." if smoker
        else "Being a non-smoker helps reduce your premium.",
        f"Your income level (DKK {income_dkk}) adjusts affordability (multiplier: {income_mult}).",
        "A standard Danish insurance tax is applied to the final premium."
    ]

    
    # Savings tips
    
    savings_tips = []

    if smoker:
        savings_tips.append("Quitting smoking can significantly reduce your insurance cost.")

    if city_mult > 1.2:
        savings_tips.append("Living in high-risk urban areas increases insurance premiums.")

    if str(predicted_category).lower() == "high":
        savings_tips.append("Improving health factors can reduce your risk category over time.")

    if not savings_tips:
        savings_tips.append("Great! You already have a low-risk profile. Keep it up 👍")

    
    # Final response
    
    return {
    "base_premium": base,
    "city_multiplier": city_mult,
    "smoker_multiplier": smoker_mult,
    "income_multiplier": income_mult,   
    "tax_factor": TAX_FACTOR,           
    "final_premium": round(final, 2),
    "currency": "DKK",
    "explanation": explanation,
    "savings_tips": savings_tips
}