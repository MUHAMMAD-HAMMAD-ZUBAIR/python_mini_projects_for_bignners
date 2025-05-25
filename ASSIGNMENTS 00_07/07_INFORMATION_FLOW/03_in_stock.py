# ------------------------------------------------------
# 🍎 Sophia's Fruit Store Inventory Checker
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program asks the user for a fruit name and checks how many
#     of that fruit are in stock in Sophia’s inventory.
# ------------------------------------------------------

# -------------------------------------
# 🔁 Function to check stock of a fruit
# -------------------------------------
def num_in_stock(fruit):
    """
    This function returns the number of fruits Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # This fruit is not in the stock list
        return 0

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # Ask user to enter the fruit name
    fruit = input("🍌 Enter a fruit: ").strip().lower()

    # Call the function to get number in stock
    stock = num_in_stock(fruit)

    # Check if the fruit is in stock
    if stock == 0:
        print("❌ This fruit is not in stock.")
    else:
        print("✅ This fruit is in stock! Here is how many:")
        print("📦", stock)

# ------------------------------------------------------
# 🛠️ Required to run main() when file is executed
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
