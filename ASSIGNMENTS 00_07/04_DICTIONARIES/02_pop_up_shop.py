# ------------------------------------------------------
# 📚 Today class based on: Fruit Shop Bill Calculator using Dictionary
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program calculates the total cost of fruits a user wants to buy.
#     It uses a dictionary to store fruit names with their prices.
#     User is asked how many of each fruit they want.
# ------------------------------------------------------

# -------------------------------------
# 🧾 1. Define fruit prices using dictionary
# -------------------------------------
fruits = {
    'apple': 1.5,
    'durian': 50,
    'jackfruit': 80,
    'kiwi': 1,
    'rambutan': 1.5,
    'mango': 5
}

# -------------------------------------
# 🛒 2. Ask user for quantity of each fruit
# -------------------------------------
total_cost = 0

for fruit_name in fruits:
    price = fruits[fruit_name]
    quantity = int(input(f"🍉 How many ({fruit_name}) do you want?: "))
    total_cost += price * quantity

# -------------------------------------
# 💰 3. Show total bill
# -------------------------------------
print(f"\n🧮 Your total is: ${total_cost}")

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
