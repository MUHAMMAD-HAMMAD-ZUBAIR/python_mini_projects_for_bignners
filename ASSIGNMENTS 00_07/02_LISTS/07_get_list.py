# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: List Input Loop – Collect and Display List
# ------------------------------------------------------

def main():
    lst = []  # 📝 Create an empty list to store user inputs

    val = input("🖊️ Enter a value: ")  # ⬇️ Get initial input from user
    while val:  # 🔄 Continue until user presses Enter without typing
        lst.append(val)  # ➕ Add the input to the list
        val = input("🖊️ Enter a value: ")  # 🔄 Ask for the next value

    print("📋 Here's the list:", lst)  # 📢 Print the final list

if __name__ == '__main__':
    main()
