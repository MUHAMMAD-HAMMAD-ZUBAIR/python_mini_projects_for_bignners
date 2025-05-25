# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Temperature Conversion (Fahrenheit to Celsius)
# ------------------------------------------------------

# -------------------------------------
# 🌡️ Program to convert Fahrenheit to Celsius
# -------------------------------------
def main():
    # Prompt user to enter temperature in Fahrenheit (float allowed)
    fahrenheit = float(input("🌡️ Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the converted temperature with units
    print(f"🌡️ Temperature: {fahrenheit}F = {celsius}C")

# ------------------------------------------------------
# Program entry point
# ------------------------------------------------------
if __name__ == "__main__":
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
