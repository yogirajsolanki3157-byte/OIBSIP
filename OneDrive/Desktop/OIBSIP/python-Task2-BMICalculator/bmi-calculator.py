def calculate_bmi(weight, height):
    return weight / (height * height)


print("===== BMI CALCULATOR =====")

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please enter positive values.")
    else:
        bmi = calculate_bmi(weight, height)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obesity")

except ValueError:
    print("Invalid input! Please enter numbers only.")