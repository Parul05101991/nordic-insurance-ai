import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Number of rows
n = 1000

# Categories
cities = ["Copenhagen","Aarhus","Odense","Aalborg","Esbjerg",
    "Randers",
    "Kolding",
    "Horsens",
    "Vejle",
    "Roskilde",
    "Herning",
    "Silkeborg",
    "Næstved",
    "Fredericia",
    "Viborg"]
occupations = ['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job']

data = []

for _ in range(n):
    age = np.random.randint(18, 66)
    weight = np.random.randint(55, 100)
    height = np.random.randint(160, 195)
    income_dkk = np.random.randint(280000, 800000)
    smoker = np.random.choice(["Yes", "No"], p=[0.30, 0.70])
    city = np.random.choice(cities)
    occupation = np.random.choice(occupations)

    # Insurance logic (simple risk-based rule)
    if income_dkk > 650000 or smoker == "Yes":
        premium = "High"
    elif income_dkk > 400000:
        premium = "Medium"
    else:
        premium = "Low"

    data.append([
        age,
        weight,
        height,
        income_dkk,
        smoker,
        city,
        occupation,
        premium
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "age",
    "weight",
    "height",
    "income_dkk",
    "smoker",
    "city",
    "occupation",
    "insurance_premium_category"
])

# Save CSV
output_file = "insurance_premium_dataset.csv"
df.to_csv(output_file, index=False)

print("✅ Dataset created successfully!")
print(f"📁 File saved as: {output_file}")