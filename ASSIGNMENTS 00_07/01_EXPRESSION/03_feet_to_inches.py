# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Unit Conversion – Feet to Inches
# ------------------------------------------------------

# -------------------------------------
# ⚙️ Constant Definition
# -------------------------------------
INCHES_IN_FOOT: int = 12  # 📐 1 foot = 12 inches

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # 📝 Ask the user to input number of feet
    feet: float = float(input("🦶 Enter number of feet: "))

    # 🔁 Convert feet to inches using the conversion factor
    inches: float = feet * INCHES_IN_FOOT

    # 📢 Display the result to the user
    print("📏 That is", inches, "inches! 📐")

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
