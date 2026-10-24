def calculate_bmi():
    print("--- BMI Calculator ---")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than zero.")
            return

        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal Weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    calculate_bmi()
