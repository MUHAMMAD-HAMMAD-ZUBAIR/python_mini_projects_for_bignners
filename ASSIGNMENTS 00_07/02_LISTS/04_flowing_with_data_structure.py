# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Mutability – Lists and Functions
# ------------------------------------------------------

def add_three_copies(my_list, data):
    # ➕ Add three copies of 'data' to the list 'my_list'
    for i in range(3):
        my_list.append(data)  # 📝 Append data without returning anything (mutability in action)

def main():
    # 📝 Get user input
    message = input("✍️ Enter a message to copy: ")

    my_list = []  # 📋 Initialize empty list
    print("🛑 List before:", my_list)  # Show list before modification

    add_three_copies(my_list, message)  # 🔄 Modify list inside function

    print("✅ List after:", my_list)  # Show list after modification (should have 3 copies)

if __name__ == "__main__":
    main()
