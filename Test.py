
from datetime import datetime, timedelta

def calculate_bmr(cisgender, weight, height, age):
    if cisgender.lower() == "m":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif cisgender.lower() == "f":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    else:
        raise ValueError("Invalid gender input. Please enter 'M' or 'F'.")
    
    return bmr

def calculate_tdee(bmr):
    activity_levels = {
        "1": 1.2,    # Sedentary
        "2": 1.375,  # Lightly active
        "3": 1.55,   # Moderately active
        "4": 1.725,  # Very active
        "5": 1.9     # Extra active
    }
    
    print("\nActivity Levels:")
    print("1. Sedentary (little to no exercise)")
    print("2. Lightly active (light exercise 1 to 3 days per week)")
    print("3. Moderately active (moderate exercise 6 to 7 days per week)")
    print("4. Very active (hard exercise every day, or exercising twice a day)")
    print("5. Extra active (very hard exercise, training, or a physical job)\n")
    
    activity_level = input("Select your activity level (1-5): ")
    if activity_level not in activity_levels:
        raise ValueError("Invalid activity level. Please choose a number between 1 and 5.")
    
    tdee = bmr * activity_levels[activity_level]
    return tdee

def calculate_bmi(weight, height):
    bmi = (weight * 703) / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

def calculate_ideal_body_weight(cisgender, height):
    if cisgender.lower() == "m":
        ibw_kg = 48 + 2.7 * (height - 60)
    elif cisgender.lower() == "f":
        ibw_kg = 45.5 + 2.2 * (height - 60)
    else:
        raise ValueError("Invalid gender input. Please enter 'M' or 'F'.")
    
    ibw_lbs = ibw_kg * 2.20462
    return ibw_lbs

def calculate_future_date(weeks):
    start_date = datetime.now()
    target_date = start_date + timedelta(weeks=weeks)
    return target_date

def main():
    print("Let's figure out your Basal Metabolic Rate (BMR)!\n")
    
    cisgender = input("At birth were you assigned (M) or (F)? ").strip().lower()
    weight = float(input("What is your weight, in pounds? ").strip())
    height = float(input("What is your height, in inches? ").strip())
    age = int(input("How old are you, in years? ").strip())

    # Calculate BMR
    bmr = calculate_bmr(cisgender, weight, height, age)
    print(f"\nYour Basal Metabolic Rate (BMR) is: {int(bmr)} calories/day.")
    
    # Calculate TDEE
    tdee = calculate_tdee(bmr)
    print(f"To maintain your current weight, you should consume {int(tdee)} calories per day.")
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    bmi_category_description = bmi_category(bmi)
    print(f"\nYour Body Mass Index (BMI) is {bmi:.2f}. You are {bmi_category_description}.")
    
    # Calculate Ideal Body Weight
    ideal_body_weight = calculate_ideal_body_weight(cisgender, height)
    print(f"\nYour ideal weight using the Hamwi Formula is approximately {round(ideal_body_weight)} lbs.")
    
    if bmi_category_description == "underweight":
        # Recommend weight gain
        print("\nSince you are underweight, it is recommended that you gain weight.")
        target_weeks = (ideal_body_weight - weight) / 2
        print(f"If you gain 2 lbs per week, it will take you {round(target_weeks)} weeks to reach your Ideal Body Weight.")
        target_date = calculate_future_date(target_weeks)
        print(f"Your target date is {target_date.strftime('%B %d, %Y')}.")
        daily_surplus = 1000  # To gain 2 lbs per week
        print(f"\nTo gain 2 lbs per week, you will need to consume {round(tdee + daily_surplus)} calories per day.")
    
    else:
        # Recommend weight loss or maintenance
        target_weeks = (weight - ideal_body_weight) / 2
        if target_weeks > 0:
            print(f"If you lose 2 lbs per week, it will take you {round(target_weeks)} weeks to reach your Ideal Body Weight.")
            target_date = calculate_future_date(target_weeks)
            print(f"Your target date is {target_date.strftime('%B %d, %Y')}.")
            daily_deficit = 1000  # To lose 2 lbs per week
            print(f"\nTo lose 2 lbs per week, you will need to consume {round(tdee - daily_deficit)} calories per day.")
        else:
            print("You are at or close to your ideal weight. Maintenance is recommended.")

if __name__ == "__main__":
    main()
