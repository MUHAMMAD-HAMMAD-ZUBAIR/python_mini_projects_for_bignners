# ╔══════════════════════════════════════════════════════════╗
# ║ 🌍 PLANETARY WEIGHT CALCULATOR                           ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                   ║
# ║ 📅 Date     : May 2025                                   ║
# ║ 📘 Concepts : Input, Conditionals, Arithmetic, Round    ║
# ╚══════════════════════════════════════════════════════════╝

# ---------------------------------------------
# 1️⃣ Define gravity factors for planets
# ---------------------------------------------
# Dictionary storing each planet's gravity relative to Earth
gravity_factors = {
    "Mercury": 0.376,  # 🌑 37.6% of Earth gravity
    "Venus": 0.889,    # ♀️ 88.9%
    "Mars": 0.378,     # ♂️ 37.8%
    "Jupiter": 2.36,   # ♃ 236.0%
    "Saturn": 1.081,   # ♄ 108.1%
    "Uranus": 0.815,   # ♅ 81.5%
    "Neptune": 1.14    # ♆ 114.0%
}

# ---------------------------------------------
# 2️⃣ Main function to calculate planetary weight
# ---------------------------------------------
def planetary_weight_calculator():
    # Welcome message to the user
    print("🌟 Welcome to the Planetary Weight Calculator! 🌟\n")

    # Prompt user to enter their weight on Earth
    weight_earth = float(input("⚖️ Enter your weight on Earth (kg or lbs): "))

    # Prompt user to enter the planet name (assumed to be correctly capitalized)
    planet = input("🪐 Enter the name of a planet (first letter capitalized): ")

    # Calculate weight on the chosen planet by multiplying Earth weight by the planet's gravity factor
    weight_planet = weight_earth * gravity_factors[planet]

    # Round the result to 2 decimal places for better readability
    weight_planet_rounded = round(weight_planet, 2)

    # Display the final calculated weight with a nice message and emoji
    print(f"\n✨ The equivalent weight on {planet} is: {weight_planet_rounded} ✨\n")

# ---------------------------------------------
# 3️⃣ Run the program if this script is executed
# ---------------------------------------------
if __name__ == "__main__":
    planetary_weight_calculator()

# ╔══════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding!       ║
# ╚══════════════════════════════════════════╝
