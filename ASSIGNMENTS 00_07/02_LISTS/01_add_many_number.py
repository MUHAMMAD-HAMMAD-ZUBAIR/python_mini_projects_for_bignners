# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Functions in Python – List Processing
# ------------------------------------------------------

# -------------------------------------
# 1️⃣ Function to sum a list of numbers
# -------------------------------------
def add_many_numbers(numbers) -> int:
    """
    🧮 Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number  # ➕ Add each number to total
    return total_so_far  # 🎯 Return the total sum


# -------------------------------------
# 2️⃣ Main function to demonstrate summing
# -------------------------------------
def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # 📝 Example list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # 🔢 Calculate sum
    print(f"🧮 Sum of {numbers} is: {sum_of_numbers} ✅")


# ------------------------------------------------------
# Required to run main() when this script executes
# ------------------------------------------------------
if __name__ == '__main__':
    main()
