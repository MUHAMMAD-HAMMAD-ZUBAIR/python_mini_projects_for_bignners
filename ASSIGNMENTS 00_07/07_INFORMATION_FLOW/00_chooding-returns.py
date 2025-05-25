# ------------------------------------------------------
# 📚 Topic: Check if a Person is an Adult
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program checks if a person is an adult (age ≥ 18)
# ------------------------------------------------------

# -------------------------------------
# 🎯 1. Constant for adult age in the U.S.
# -------------------------------------
ADULT_AGE: int = 18  # Legal adult age in the United States

# -------------------------------------
# 👤 2. Function to check if age is adult
# -------------------------------------
def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    return False

# -------------------------------------
# 📥 3. Main function to get input and call helper
# -------------------------------------
def main():
    age = int(input("🧓 How old is this person?: "))  # Ask user's age
    result = is_adult(age)  # Check if adult
    print(f"✅ Is adult? {result}")

# -------------------------------------
# 🚀 Start the program
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
