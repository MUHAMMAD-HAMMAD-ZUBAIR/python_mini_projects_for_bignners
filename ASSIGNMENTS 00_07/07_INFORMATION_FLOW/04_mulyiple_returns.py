# ------------------------------------------------------
# 🧾 User Signup Data Collection Program
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Description:
#     This program collects a user's first name, last name,
#     and email address, and returns them as a tuple.
# ------------------------------------------------------

# -------------------------------------
# 🔁 Function to collect user info
# -------------------------------------
def get_user_info():
    # Ask for user's first name
    first_name: str = input("📝 What is your first name?: ")
    
    # Ask for user's last name
    last_name: str = input("📝 What is your last name?: ")
    
    # Ask for user's email address
    email_address: str = input("📧 What is your email address?: ")
    
    # Return all three values as a tuple
    return first_name, last_name, email_address

# -------------------------------------
# 🚀 Main function to run the program
# -------------------------------------
def main():
    # Get the tuple of user data
    user_data = get_user_info()
    
    # Display the received data
    print("✅ Received the following user data:", user_data)

# ------------------------------------------------------
# 🛠️ Run the main() function when this file is executed
# ------------------------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of program
# ------------------------------------------------------
