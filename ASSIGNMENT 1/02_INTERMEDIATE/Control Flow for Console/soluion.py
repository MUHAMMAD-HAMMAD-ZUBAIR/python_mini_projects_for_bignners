# ╔══════════════════════════════════════════════════════════╗
# ║ 🎮 HIGH-LOW GAME IN PYTHON                               ║
# ║ 👨‍💻 Author   : Muhammad Hammad Zubair                   ║
# ║ 📅 Date     : May 2025                                   ║
# ║ 📘 Concepts : Random Numbers, Input Validation, Loops    ║
# ╚══════════════════════════════════════════════════════════╝

# ---------------------------------------------
# 1️⃣ Import Required Modules
# ---------------------------------------------
import random  # 🎲 To generate random numbers for the game
import time    # ⏱️ Used to add small delays to improve user experience

# ---------------------------------------------
# 2️⃣ Define Constants and Configuration
# ---------------------------------------------
TOTAL_ROUNDS = 5  # 🔢 Number of rounds the player will play
MIN_NUM = 1       # Minimum number value in the game
MAX_NUM = 100     # Maximum number value in the game

# ---------------------------------------------
# 3️⃣ Input Validation Function
# ---------------------------------------------
def get_user_guess():
    """
    Continuously prompt the user until they enter a valid guess:
    either 'higher' or 'lower' (case-insensitive).
    """
    while True:
        user_input = input("🔍 Do you think your number is HIGHER or LOWER than the computer's? ").strip().lower()
        if user_input in ['higher', 'lower']:
            return user_input  # Valid input, return it
        # If invalid, notify user and ask again
        print("⚠️ Invalid input! Please type 'higher' or 'lower'.")

# ---------------------------------------------
# 4️⃣ Main Game Function
# ---------------------------------------------
def play_high_low_game():
    # Introduction message
    print("\n🎉 WELCOME TO THE HIGH-LOW GAME 🎉")
    print("🔢 Try to guess whether your number is HIGHER or LOWER than the computer's.\n")

    score = 0  # 🧮 Initialize the player's score to zero

    # Loop through the total number of rounds
    for round_num in range(1, TOTAL_ROUNDS + 1):
        print(f"\n🔁 ROUND {round_num} of {TOTAL_ROUNDS}")  # Display current round number
        print("🎲 Rolling the numbers...")

        time.sleep(1)  # ⏳ Pause for 1 second to build suspense

        # Generate random numbers for user and computer
        user_num = random.randint(MIN_NUM, MAX_NUM)
        computer_num = random.randint(MIN_NUM, MAX_NUM)

        print(f"📍 Your number: {user_num}")  # Show user's number
        user_guess = get_user_guess()        # Ask user to guess higher or lower

        print(f"🤖 Computer's number: {computer_num}")  # Reveal computer's number

        # ---------------------------------------------
        # 🧠 Game Logic to determine if user's guess is correct
        # ---------------------------------------------
        if user_num == computer_num:
            print("⚖️ Both numbers are the same! No points awarded.")  # Tie case
        elif user_guess == 'higher' and user_num > computer_num:
            print("✅ Correct! Your number is higher.")  # User guessed higher correctly
            score += 1
        elif user_guess == 'lower' and user_num < computer_num:
            print("✅ Correct! Your number is lower.")  # User guessed lower correctly
            score += 1
        else:
            print("❌ Incorrect guess!")  # User's guess was wrong

        print(f"🏆 Current Score: {score}")  # Show updated score after each round

    # ---------------------------------------------
    # 5️⃣ Final Results and Feedback after all rounds are done
    # ---------------------------------------------
    print("\n🧾 GAME OVER!")
    print("═══════════════════════════════")
    print(f"🔚 Total Rounds Played : {TOTAL_ROUNDS}")
    print(f"🎯 Final Score         : {score}")

    # Provide feedback based on final score
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
    play_high_low_game()  # Run the main game function when script runs

# ╔══════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding!       ║
# ╚══════════════════════════════════════════╝
