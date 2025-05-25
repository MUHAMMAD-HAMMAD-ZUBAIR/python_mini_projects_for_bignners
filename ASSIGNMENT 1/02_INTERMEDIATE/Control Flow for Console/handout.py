# ╔══════════════════════════════════════════════════════════╗
# ║ 🎮 HIGH-LOW GAME IN PYTHON                               ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                   ║
# ║ 📅 Date     : May 2025                                   ║
# ║ 📘 Concepts : Random Numbers, Input Validation, Loops    ║
# ╚══════════════════════════════════════════════════════════╝

# ---------------------------------------------
# 1️⃣ Import Required Modules
# ---------------------------------------------
import random  # 🎲 For generating random numbers for the game
import time    # ⏱️ To add small delays for better user experience

# ---------------------------------------------
# 2️⃣ Define Constants and Configuration
# ---------------------------------------------
TOTAL_ROUNDS = 5  # Number of rounds the player will play
MIN_NUM = 1       # Minimum possible random number
MAX_NUM = 100     # Maximum possible random number

# ---------------------------------------------
# 3️⃣ Input Validation Function
# ---------------------------------------------
def get_user_guess():
    """
    Prompt the user to enter their guess: 'higher' or 'lower'.
    Keeps asking until a valid input is entered (case-insensitive).
    """
    while True:
        user_input = input("🔍 Do you think your number is HIGHER or LOWER than the computer's? ").strip().lower()
        if user_input in ['higher', 'lower']:
            return user_input  # Return valid input to the caller
        # If invalid, inform the user and ask again
        print("⚠️ Invalid input! Please type 'higher' or 'lower'.")

# ---------------------------------------------
# 4️⃣ Main Game Function
# ---------------------------------------------
def play_high_low_game():
    # Welcome message and game instructions
    print("\n🎉 WELCOME TO THE HIGH-LOW GAME 🎉")
    print("🔢 Try to guess whether your number is HIGHER or LOWER than the computer's.\n")

    score = 0  # Initialize the player's score

    # Loop for the total number of rounds
    for round_num in range(1, TOTAL_ROUNDS + 1):
        print(f"\n🔁 ROUND {round_num} of {TOTAL_ROUNDS}")
        print("🎲 Rolling the numbers...")

        time.sleep(1)  # Pause for 1 second to build suspense

        # Generate random numbers for the user and computer
        user_num = random.randint(MIN_NUM, MAX_NUM)
        computer_num = random.randint(MIN_NUM, MAX_NUM)

        # Show the user's number
        print(f"📍 Your number: {user_num}")
        # Ask the user to guess higher or lower
        user_guess = get_user_guess()

        # Reveal the computer's number
        print(f"🤖 Computer's number: {computer_num}")

        # ---------------------------------------------
        # 🧠 Game Logic to check if the user's guess was correct
        # ---------------------------------------------
        if user_num == computer_num:
            # Tie case: numbers are the same
            print("⚖️ Both numbers are the same! No points awarded.")
        elif user_guess == 'higher' and user_num > computer_num:
            # User guessed higher correctly
            print("✅ Correct! Your number is higher.")
            score += 1  # Increase score by 1
        elif user_guess == 'lower' and user_num < computer_num:
            # User guessed lower correctly
            print("✅ Correct! Your number is lower.")
            score += 1  # Increase score by 1
        else:
            # User guessed incorrectly
            print("❌ Incorrect guess!")

        # Show the current score after each round
        print(f"🏆 Current Score: {score}")

    # ---------------------------------------------
    # 5️⃣ Final Results and Feedback after all rounds are finished
    # ---------------------------------------------
    print("\n🧾 GAME OVER!")
    print("═══════════════════════════════")
    print(f"🔚 Total Rounds Played : {TOTAL_ROUNDS}")
    print(f"🎯 Final Score         : {score}")

    # Feedback based on player's final score
    if score == TOTAL_ROUNDS:
        print("🌟 Perfect Score! You're a High-Low Champion!")
    elif score >= TOTAL_ROUNDS // 2:
        print("👏 Great Job! You know your luck well!")
    else:
        print("💡 Keep practicing! Better luck next time.")

    print("🙌 Thanks for playing the High-Low Game!\n")

# ---------------------------------------------
# 🚀 Start the Game
# ---------------------------------------------
if __name__ == '__main__':
    play_high_low_game()  # Call the main function to start the game

# ╔══════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding!       ║
# ╚══════════════════════════════════════════╝
