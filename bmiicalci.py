def calculate_bmi(weight, height):
    """Calculate the using weight (kg) / height^2 (m^2) to determine BMI"""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify the BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator!")
    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
    
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your classification is: {category}")

    except ValueError:
        print(" Enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()