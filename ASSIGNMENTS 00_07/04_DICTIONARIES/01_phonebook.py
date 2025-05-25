# ------------------------------------------------------
# 📚 Today class based on: Phonebook using Dictionary
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program uses a dictionary to store and lookup phone numbers.
# ------------------------------------------------------

# -------------------------------------
# 📥 1. Function to read phone numbers into a dictionary
# -------------------------------------
def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Stops when the user inputs a blank name.
    Returns the phonebook dictionary.
    """
    phonebook = {}  # Create empty phonebook dictionary

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number  # Store the number with the name as key

    return phonebook

# -------------------------------------
# 🖨️ 2. Function to print all entries in the phonebook
# -------------------------------------
def print_phonebook(phonebook):
    """
    Prints all the names and their corresponding phone numbers.
    """
    print("\n📖 Phonebook Entries:")
    for name in phonebook:
        print(f"📱 {name} -> {phonebook[name]}")

# -------------------------------------
# 🔍 3. Function to lookup phone numbers by name
# -------------------------------------
def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers by entering a name.
    Stops when the user inputs a blank name.
    """
    while True:
        name = input("\nEnter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"❌ {name} is not in the phonebook.")
        else:
            print(f"📞 Number for {name}: {phonebook[name]}")

# -------------------------------------
# ▶️ 4. Main function to run the program
# -------------------------------------
def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
    print("\n✅ End of program 👋")

# ------------------------------------------------------
# Boilerplate to call main function
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
