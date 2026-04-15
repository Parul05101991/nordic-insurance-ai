# Denmark insurance assumptions --->rule-based risk adjustment layer
#Final premium = Base premium × risk multipliers × tax factor


# Base assumptions

SMOKER_MULTIPLIER = 1.4   # more realistic EU insurance uplift
TAX_FACTOR = 1.20         # Denmark insurance tax average

BASE_PREMIUM = {
    "Low": 300,
    "Medium": 600,
    "High": 1000
}

CITY_RISK_SCORE = {
    "Copenhagen": 1.25,
    "Aarhus": 1.15,
    "Odense": 1.05,
    "Aalborg": 1.05
}


