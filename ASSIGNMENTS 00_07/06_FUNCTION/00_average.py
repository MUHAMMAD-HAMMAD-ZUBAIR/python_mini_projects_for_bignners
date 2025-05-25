# ------------------------------------------------------
# 📚 Today class based on: Python Functions - Average Calculation
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program demonstrates how to write a function that
#     calculates the average of two numbers.
# ------------------------------------------------------

# -------------------------------------
# 🧮 1. Define average function
# -------------------------------------
def average(a: float, b: float) -> float:
    """
    Returns the number which is half way between a and b.
    """
    total = a + b
    return total / 2

# -------------------------------------
# 🔄 2. Main function to test average
# -------------------------------------
def main():
    avg_1 = average(0, 10)    # Average of 0 and 10
    avg_2 = average(8, 10)    # Average of 8 and 10
    
    final = average(avg_1, avg_2)  # Average of previous averages
    
    print("📊 avg_1:", avg_1)       # Output avg_1
    print("📊 avg_2:", avg_2)       # Output avg_2
    print("🎯 final average:", final)  # Output final average

# ------------------------------------------------------
# ▶️ Start the program
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
