# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Einstein’s E = mc² – Mass-Energy Equivalence
# ------------------------------------------------------

# -------------------------------------
# ⚙️ Constant for Speed of Light
# -------------------------------------
C: int = 299_792_458  # Speed of light in meters per second (m/s)

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # Ask user to input mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula: E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Show the full process
    print("\ne = m * C^2...")
    print("m =", mass_in_kg, "kg")
    print("C =", C, "m/s")
    print(f"\n⚡ {energy_in_joules} joules of energy!")

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
