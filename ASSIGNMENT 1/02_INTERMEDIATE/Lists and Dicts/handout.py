# ╔════════════════════════════════════════════════════════════════════╗
# ║ 🍎🍌🍊 LIST PRACTICE & INDEX GAME WITH THEMES                     ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                            ║
# ║ 📅 Date     : May 2025                                            ║
# ║ 📘 Concepts : Lists, Indexing, Slicing, Input, Error Handling     ║
# ╚════════════════════════════════════════════════════════════════════╝


# ---------------------------------------------
# 1️⃣ Problem 1: List Practice
# ---------------------------------------------
def list_practice():
    print("\n🍇 --- Problem 1: List Practice --- 🍇")

    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print(f"Length of fruit_list: {len(fruit_list)}")

    # Add 'mango' at the end
    fruit_list.append('mango')

    # Print the updated list
    print("Updated fruit_list:", fruit_list)


# ---------------------------------------------
# 2️⃣ Problem 2: Index Game
# ---------------------------------------------
def access_element(lst, index):
    # Safely access element at given index
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "❌ Index out of range!"

def modify_element(lst, index, new_value):
    # Safely modify element at given index
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"✅ Element at index {index} modified."
    else:
        return "❌ Index out of range!"

def slice_list(lst, start_index, end_index):
    # Safely slice list with clamped indices
    start = max(0, start_index)
    end = min(len(lst), end_index)
    if start >= end:
        return "❌ Invalid slice indices!"
    return lst[start:end]

def index_game():
    print("\n🎮 --- Problem 2: Index Game --- 🎮")
    
    # Initialize a mixed list
    game_list = [10, "cat", 3.14, "dog", 42]

    while True:
        print("\n🔹 Current list:", game_list)
        print("\nChoose operation:")
        print("1️⃣ Access element")
        print("2️⃣ Modify element")
        print("3️⃣ Slice list")
        print("4️⃣ Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            try:
                idx = int(input("🔢 Enter index to access: "))
                result = access_element(game_list, idx)
                print("➡️ Result:", result)
            except ValueError:
                print("❌ Please enter a valid integer index!")

        elif choice == "2":
            try:
                idx = int(input("🔢 Enter index to modify: "))
                new_val = input("✏️ Enter new value: ")
                # Attempt to convert input to int or float if possible
                if new_val.isdigit():
                    new_val = int(new_val)
                else:
                    try:
                        new_val = float(new_val)
                    except ValueError:
                        pass  # keep as string if no conversion
                message = modify_element(game_list, idx, new_val)
                print(message)
            except ValueError:
                print("❌ Please enter a valid integer index!")

        elif choice == "3":
            try:
                start_idx = int(input("🔢 Enter start index: "))
                end_idx = int(input("🔢 Enter end index: "))
                sliced = slice_list(game_list, start_idx, end_idx)
                print("➡️ Sliced list:", sliced)
            except ValueError:
                print("❌ Please enter valid integer indices!")

        elif choice == "4":
            print("👋 Goodbye! Thanks for playing the Index Game.")
            break
        else:
            print("❌ Invalid choice, please select from 1-4.")

# ---------------------------------------------
# 🏁 Run the complete program
# ---------------------------------------------
if __name__ == "__main__":
    print("📝 Welcome to the List Practice & Index Game Program!")
    list_practice()
    index_game()

# ╔════════════════════════════════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding & Learning!                      ║
# ╚════════════════════════════════════════════════════════════════════╝
