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

# ---------------------------------------------
# 2️⃣ Define Constants and Configuration
# ---------------------------------------------
NUM_ROUNDS = 5  # 🔢 Number of rounds the player will play
MIN_NUM = 1     # Minimum number value in the game
MAX_NUM = 100   # Maximum number value in the game

# ---------------------------------------------
# 3️⃣ Main Game Function
# ---------------------------------------------
def main():
    print("\n🎉 Welcome to the High-Low Game! 🎉")
    print('--------------------------------\n')
    
    score = 0  # 🧮 Initialize player's score
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"🔁 Round {round_num} of {NUM_ROUNDS}")
        
        # Generate random numbers for player and computer
        your_num = random.randint(MIN_NUM, MAX_NUM)
        computer_num = random.randint(MIN_NUM, MAX_NUM)
        
        print(f"📍 Your number is: {your_num}")
        
        # Get user choice with input validation
        choice = input("❓ Do you think your number is higher or lower than the computer's? ").strip().lower()
        while choice not in ['higher', 'lower']:
            choice = input("⚠️ Invalid input! Please enter 'higher' or 'lower': ").strip().lower()
        
        # Check if guess is correct
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print(f"✅ You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"❌ That's incorrect. The computer's number was {computer_num}")
        
        print(f"🏆 Your score is now: {score}\n")
    
    # Final score and feedback
    print("🎯 Game Over!")
    print(f"🔚 Your final score is {score} out of {NUM_ROUNDS}")
    if score == NUM_ROUNDS:
        print("🌟 Perfect Score! You're a High-Low Champion!")
    elif score > NUM_ROUNDS // 2:
        print("👏 Great job! You know your luck well!")
    else:
        print("💡 Keep practicing! Better luck next time.")
    
    print("\n🙌 Thanks for playing the High-Low Game!\n")

# ---------------------------------------------
# 🚀 Start the game
# ---------------------------------------------
if __name__ == "__main__":
    main()

# ╔══════════════════════════════════════════╗
# ║ ✅ End of Program - Happy Coding!       ║
# ╚══════════════════════════════════════════╝
