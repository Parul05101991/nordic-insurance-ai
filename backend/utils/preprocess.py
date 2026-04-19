from shared.config.city_tiers import tier_1_cities, tier_2_cities


def calculate_bmi(weight: float, height: float) -> float:
    return weight / ((height / 100) ** 2)


def get_lifestyle_risk(smoker: bool, bmi: float) -> str:
    if smoker and bmi >= 30:
        return "very_high"
    elif smoker and bmi >= 27:
        return "high"
    elif bmi >= 27:
        return "medium"
    else:
        return "low"
    

def get_age_group(age: int) -> str:
    if age < 25:
        return "young"
    elif age < 45:
        return "adult"
    elif age < 60:
        return "middle_aged"
    else:
        return "senior"
    



def get_city_tier(city: str) -> int:
    city = city.strip().title()

    if city in tier_1_cities:
        return 1
    elif city in tier_2_cities:
        return 2
    else:
        return 3


def build_features(data):

    bmi = calculate_bmi(data.weight, data.height)
    lifestyle_risk = get_lifestyle_risk(data.smoker, bmi)
    age_group = get_age_group(data.age)
    city_tier = get_city_tier(data.city)

    return {
        "age": data.age,

       
        "income_dkk": data.income_dkk,

        "occupation": data.occupation,
        "smoker": data.smoker,
        "bmi": bmi,
        "lifestyle_risk": lifestyle_risk,
        "age_group": age_group,
        "city_tier": city_tier
    }