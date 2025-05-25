# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Age Riddle Solution
# ------------------------------------------------------

def main():
    # 🧑 Anton's age is 21
    anton: int = 21

    # 👩 Beth is 6 years older than Anton
    beth: int = anton + 6

    # 👨‍🦳 Chen is 20 years older than Beth
    chen: int = beth + 20

    # 🧔 Drew is as old as Chen plus Anton combined
    drew: int = chen + anton

    # 👦 Ethan is the same age as Chen
    ethan: int = chen

    # 🖨️ Print everyone's age carefully with correct format
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


# ------------------------------------------------------
# Program entry point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
