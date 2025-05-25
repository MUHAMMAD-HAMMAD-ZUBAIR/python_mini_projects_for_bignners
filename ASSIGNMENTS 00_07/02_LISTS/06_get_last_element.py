# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: List Access – Getting Last Element
# ------------------------------------------------------

def get_last_element(lst):
    """
    🖨️ Prints the last element of the provided list lst.
    Assumes lst is non-empty.
    """
    # Using negative indexing to get last element
    print(f"🎯 Last element: {lst[-1]}")

def get_lst():
    """
    📝 Prompts the user to enter elements one by one.
    User can stop by pressing enter without input.
    Returns the list of entered elements.
    """
    lst = []
    elem = input("🖊️ Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("🖊️ Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # 📥 Get list input from user
    get_last_element(lst)  # 🎯 Print last element of the list

if __name__ == '__main__':
    main()
