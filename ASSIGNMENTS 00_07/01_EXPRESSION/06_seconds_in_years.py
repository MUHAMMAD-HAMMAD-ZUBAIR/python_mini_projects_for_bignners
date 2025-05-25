# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Topic: Constants & Multiplication Logic
# ------------------------------------------------------

# 🔢 Constants for time calculations
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # 🧮 Calculate total seconds in a year
    seconds_per_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # 📢 Display result
    print("⏱️ There are " + str(seconds_per_year) + " seconds in a year! 🎉")

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
