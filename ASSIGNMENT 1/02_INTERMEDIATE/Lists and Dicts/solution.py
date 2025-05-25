# ╔════════════════════════════════════════════════════════════════╗
# ║ 🍎 LIST PRACTICE & INDEX GAME                                  ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                        ║
# ║ 📅 Date     : May 2025                                         ║
# ║ 📘 Concepts : Lists, Indexing, Exception Handling, User Input  ║
# ╚════════════════════════════════════════════════════════════════╝

def list_practice():
    print("🍎 --- List Practice --- 🍎")

    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print length of the list
    print(f"📏 Length of fruit_list: {len(fruit_list)}")

    # Add 'mango' to the list
    fruit_list.append('mango')

    # Print updated list with fruit emojis
    print("🆕 Updated fruit_list:")
    fruit_emojis = {
        'apple': '🍏', 'banana': '🍌', 'orange': '🍊',
        'grape': '🍇', 'pineapple': '🍍', 'mango': '🥭'
    }
    for fruit in fruit_list:
        emoji = fruit_emojis.get(fruit, "🍉")  # default emoji if fruit missing
        print(f"{emoji} {fruit}")

    print("\n")  # Spacer


def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "❌ Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return "✅ Element modified successfully."
    except IndexError:
        return "❌ Index out of range."

def slice_list(lst, start, end):
    # No IndexError for slicing in Python, but handle invalid input
    if start < 0 or end > len(lst) or start > end:
        return "❌ Invalid slice indices."
    return lst[start:end]

def index_game():
    print("🎮 --- Index Game --- 🎮")
    lst = [1, 2, 3, 4, 5]  # Starting list

    while True:
        print(f"\n🔹 Current list: {lst}")
        print("⚙️ Choose operation:")
        print("1️⃣ Access element")
        print("2️⃣ Modify element")
        print("3️⃣ Slice list")
        print("4️⃣ Exit")
        choice = input("➡️ Enter choice (1-4): ").strip()

        if choice == "1":
            try:
                index = int(input("🔢 Enter index to access: "))
                result = access_element(lst, index)
                print(f"🔍 Result: {result}")
            except ValueError:
                print("❌ Please enter a valid integer index.")

        elif choice == "2":
            try:
                index = int(input("🔢 Enter index to modify: "))
                new_value = input("✏️ Enter new value: ")
                # Try to convert new_value to int if possible
                if new_value.isdigit():
                    new_value = int(new_value)
                result = modify_element(lst, index, new_value)
                print(result)
            except ValueError:
                print("❌ Please enter a valid integer index.")

        elif choice == "3":
            try:
                start = int(input("🔢 Enter start index: "))
                end = int(input("🔢 Enter end index: "))
                sliced = slice_list(lst, start, end)
                print(f"🔎 Sliced list: {sliced}")
            except ValueError:
                print("❌ Please enter valid integer indices.")

        elif choice == "4":
            print("👋 Goodbye! Thanks for playing the Index Game.")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == '__main__':
    print("📝 Welcome to the List Practice & Index Game Program!\n")
    list_practice()
    index_game()
