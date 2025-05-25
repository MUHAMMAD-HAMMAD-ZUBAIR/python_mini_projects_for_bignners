# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: List Shortening by Removing Elements from End
# ------------------------------------------------------

MAX_LENGTH: int = 3  # 🎯 Maximum allowed length of the list

def shorten(lst):
    """
    Removes elements from the end of the list until its length is MAX_LENGTH.
    Prints each removed element.
    If the list length is already less or equal to MAX_LENGTH, no changes are made.
    """
    # 🔄 Loop until the list length is within the allowed MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # ❌ Remove the last element from the list
        print(f"Removed: {last_elem} 🗑️")  # 🖨️ Print the removed element

# ------------------------------------------------------
# Helper function to collect user input into a list
def get_lst():
    """
    Prompt the user to enter elements one by one.
    Stops when user presses enter without input.
    Returns the list of entered elements.
    """
    lst = []  # Initialize empty list
    elem = input("Please enter an element of the list or press enter to stop: ")  # Get first element
    while elem != "":  # Continue until empty input
        lst.append(elem)  # Add element to list
        elem = input("Please enter an element of the list or press enter to stop: ")  # Get next element
    return lst  # Return the complete list

def main():
    lst = get_lst()  # Get list from user input
    shorten(lst)  # Shorten list if needed and print removed elements

if __name__ == '__main__':
    main()  # Run main function if this file is executed directly
