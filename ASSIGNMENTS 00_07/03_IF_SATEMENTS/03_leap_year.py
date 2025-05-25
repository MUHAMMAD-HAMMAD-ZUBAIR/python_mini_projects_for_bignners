# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 🏫 Class: Five
# 📅 Date: May 2025
# 📘 Lesson: Leap Year Checker with User Input and Emojis
# ------------------------------------------------------

def main():
    # Ask the user for a year
    year = int(input("📅 Please input a year: "))

    # Leap year logic
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("🎉 That's a leap year! 🥳")
            else:
                print("❌ That's not a leap year. 😕")
        else:
            print("🎉 That's a leap year! 🥳")
    else:
        print("❌ That's not a leap year. 😕")

# Required for standalone run
if __name__ == '__main__':
    main()
