# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: While Loops and Input Handling
# ------------------------------------------------------

def main():
    # 📝 Ask user to enter a starting number
    curr_value = int(input("🔢 Enter a number to double: "))
    
    # 🔄 Loop until curr_value reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2  # ✖️ Double the current value
        print(f"➡️ {curr_value}")    # 🖨️ Print the doubled value

if __name__ == '__main__':
    main()
    
# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
