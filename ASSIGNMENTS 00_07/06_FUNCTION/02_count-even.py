# ------------------------------------------------------
# 📚 Today class based on: Counting Even Numbers in a List
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program prompts the user to enter integers until they press enter,
#     then counts and prints how many even numbers were entered.
# ------------------------------------------------------

# -------------------------------------
# 🧮 1. count_even(lst) function
# -------------------------------------
def count_even(lst):
    """
    Counts and prints how many even numbers are in the list.
    """
    count = 0  # 🔢 Count of even numbers
    for num in lst:  # 🔄 Loop through each number in the list
        if num % 2 == 0:  # ✅ Check if number is even
            count += 1  # ➕ Increment count if even

    print("⚖️ Number of even numbers:", count)  # 🖨️ Print the count

# -------------------------------------
# 📝 2. get_list_of_ints() function
# -------------------------------------
def get_list_of_ints():
    """
    Prompts the user to enter integers until pressing enter, then returns the list.
    """
    lst = []  # 📋 Initialize empty list
    user_input = input("Enter an integer or press enter to stop: ")  # ⌨️ User input prompt
    while user_input != "":  # 🔁 Continue until user presses enter without input
        lst.append(int(user_input))  # 🔢 Add the integer to the list
        user_input = input("Enter an integer or press enter to stop: ")  # ⌨️ Next input

    return lst  # 📤 Return the list of integers

# -------------------------------------
# ▶️ 3. main() function - Program starts here
# -------------------------------------
def main():
    lst = get_list_of_ints()  # 📝 Get list of integers from user
    count_even(lst)  # 🧮 Count and print even numbers

# ------------------------------------------------------
# ▶️ Program Entry Point
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
