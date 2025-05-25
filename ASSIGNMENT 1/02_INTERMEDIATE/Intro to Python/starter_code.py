# ╔══════════════════════════════════════════════════════════╗
# ║ 🌍 PLANETARY WEIGHT CALCULATOR                           ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                   ║
# ║ 📅 Date     : May 2025                                   ║
# ║ 📘 Concepts : Input, Conditionals, Arithmetic, Round    ║
# ╚══════════════════════════════════════════════════════════╝

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

def main():
    print("🌟 Welcome to the Planetary Weight Calculator! 🌟\n")

    # Ask user for their Earth weight
    earth_weight = float(input("⚖️ Enter your weight on Earth (kg or lbs): "))

    # Ask user for the planet name
    planet = input("🪐 Enter the name of a planet (first letter capitalized): ")

    # Calculate equivalent weight on the chosen planet
    planetary_weight = earth_weight * gravity_factors[planet]

    # Round to 2 decimal places
    planetary_weight_rounded = round(planetary_weight, 2)

    # Show the result with emojis and nice formatting
    print(f"\n✨ The equivalent weight on {planet} is: {planetary_weight_rounded} ✨\n")

if __name__ == "__main__":
    main()

# ╔══════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding!       ║
# ╚══════════════════════════════════════════╝
