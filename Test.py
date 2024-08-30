from datetime import datetime, timedelta


def calculateBmr(cisgender,weight,height,age):
    if cisgender == "M" or cisgender == "m":
        bmr = 66+(6.23*weight)+(12.7*height)-(6.8*float(age))
    elif cisgender == "F" or cisgender == "f":
        bmr = 655+(4.35*weight)+(4.7*height)-(4.7*float(age))
    print("\nYour Basal Metabolic Rate is: ", int(bmr))
    tdee(bmr)

def tdee(bmr):
    activity = 1.0
    tdee = 1.0
    print("\n1. Sedentary (little to no exercise)")
    print("2. Lightly active (light exercise 1 to 3 days per week)")
    print("3. Moderately active (moderate exercise 6 to 7 days per week)")
    print("4. Very active (hard exercise every day, or exercising twice a day)")
    print("5. Extra active (very hard exercise, training, or a physical job)\n")
    actvityLevel = input("How active are you?  ")
    if actvityLevel == "1":
        tdee = bmr*1.2
    elif actvityLevel == "2":
        tdee = bmr*1.375
    elif actvityLevel == "3":
        tdee = bmr*1.55
    elif actvityLevel == "4":
        tdee = bmr*1.725
    elif actvityLevel == "5":
        tdee = bmr*1.9
    print("\nTo maintain your current weight, you should consume", int(tdee), "calories per day.")

def bmiCalculator(weight,height):
    bmi = (weight*703)/(height**2)
    print("\nYour Body Mass Index (BMI) is",int(bmi),".\n")
    if bmi <= 18.5:
        print("You are underweight.")
    elif bmi > 18.5 and bmi < 24.9:
        print("You are normal weight.")
    elif bmi > 25 and bmi < 29.9:
        print("You are overwieght.")
    elif bmi >30:
        print("You are obese.")

def futureDate(targetWeeks):
    startDate = datetime.now()
    targetDate = startDate + timedelta(weeks=targetWeeks)
    return targetDate

def weightLoss(cisgender,height,weight):
    if cisgender == "M" or cisgender == "m":
        idealBodyWeight = 48+2.7*(height-60)
    elif cisgender == "F" or cisgender == "f":
        idealBodyWeight = 45.5+2.2*(height-60)
    idealBodyWeight = idealBodyWeight*2.20462
    print("\nYour ideal weight using the Hamwi Formula is",round(idealBodyWeight),"lbs.")
    targetWeeks = (weight-idealBodyWeight)/2
    print("\nIf you lose 2 lbs per week, it will take you",round(targetWeeks),"weeks to reach your Ideal Body Weight.")
    print("\nYour target date is",futureDate(targetWeeks).strftime("%B %d, %Y"),".")
    calorieDeficit(weight,idealBodyWeight)

def calorieDeficit(weight,idealBodyWeight):
    dailyDeficit = (2*3500)/7
    print("\nTo lose 2lbs per week, you will need to consume",round(dailyDeficit),"fewer calories a day.\n\n")
    

def main():
    print("\n\n\nLet's figure out your Basal Metabolic Rate (BMR)!\n")
    cisgender = input("At birth were you assigned (M) or (F)?  ")
    weight = float(input("What is your weight, in pounds?  "))
    height = float(input("What is your height, in inches?  "))
    age = input("How old are you, in years?  ")
    calculateBmr(cisgender,weight,height,age)
    bmiCalculator(weight,height)
    weightLoss(cisgender,int(height),int(weight))

main()