import time

print("=" * 50)
print("        ADVANCED BMI CALCULATOR")
print("=" * 50)

while True:

    try:
        # Weight Input
        weight = float(input("\nEnter your weight (kg): "))

        if weight <= 0:
            print("❌ Weight must be greater than 0.")
            continue

        # Height Unit Choice
        print("\nChoose height unit:")
        print("1. Meters")
        print("2. Centimeters")
        print("3. Inches")

        choice = input("Enter your choice (1/2/3): ")

        # Height Conversion
        if choice == "1":
            height = float(input("Enter height in meters: "))

        elif choice == "2":
            height_cm = float(input("Enter height in centimeters: "))
            height = height_cm / 100

        elif choice == "3":
            height_inch = float(input("Enter height in inches: "))
            height = height_inch * 0.0254

        else:
            print("❌ Invalid choice.")
            continue

        # Height Validation
        if height <= 0:
            print("❌ Height must be greater than 0.")
            continue

        # BMI Calculation
        bmi = weight / (height ** 2)

        print("\nCalculating BMI...")
        time.sleep(1)

        print(f"\n✅ Your BMI is: {bmi:.2f}")

        # BMI Classification
        if bmi < 18.5:
            category = "Underweight"
            advice = "Increase nutritious calorie intake and exercise regularly."

        elif bmi < 25:
            category = "Normal Weight"
            advice = "Excellent! Maintain your healthy lifestyle."

        elif bmi < 30:
            category = "Overweight"
            advice = "Try regular workouts and balanced nutrition."

        elif bmi < 35:
            category = "Obese"
            advice = "Focus on healthy eating and physical activity."

        else:
            category = "Severely Obese"
            advice = "Consult a healthcare professional."

        # Display Results
        print(f"📌 Category: {category}")
        print(f"💡 Health Advice: {advice}")

        # BMI Scale
        print("\n========== BMI SCALE ==========")
        print("Below 18.5       -> Underweight")
        print("18.5 to 24.9     -> Normal Weight")
        print("25 to 29.9       -> Overweight")
        print("30 to 34.9       -> Obese")
        print("35 and above     -> Severely Obese")

        # Continue or Exit
        again = input("\nDo you want to calculate again? (yes/no): ").lower()

        if again != "yes":
            print("\n👋 Thank you for using the BMI Calculator!")
            break

    except ValueError:
        print("❌ Please enter valid numeric values.")
