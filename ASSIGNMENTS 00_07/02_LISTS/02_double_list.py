# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: List Manipulation – Doubling List Elements
# ------------------------------------------------------

def main():
    numbers: list[int] = [1, 2, 3, 4]  # 🔢 Original list of numbers

    # 🔄 Loop through list indices to double each element
    for i in range(len(numbers)):
        elem_at_index = numbers[i]  # 👉 Current element
        numbers[i] = elem_at_index * 2  # ✖️ Double the element and update list

    print(f"🚀 Doubled numbers list: {numbers}")  # 📤 Output the doubled list


# ------------------------------------------------------
# This line runs main() when script is executed directly
# ------------------------------------------------------
if __name__ == '__main__':
    main()
