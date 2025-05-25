# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Topic: Strings & User Input – Mad Libs Game
# ------------------------------------------------------

# 🌟 Sentence starter
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

# -------------------------------------
# 🚀 Main Function
# -------------------------------------
def main():
    # 🎯 Ask for user input
    adjective: str = input("🎨 Please type an *adjective* and press enter: ")
    noun: str = input("🪴 Please type a *noun* and press enter: ")
    verb: str = input("🕊️ Please type a *verb* and press enter: ")

    # 🧩 Form the final sentence
    final_sentence: str = SENTENCE_START + adjective + " " + noun + " " + verb + "!"

    # 📢 Print the fun story
    print("\n🎉 Here's your Mad Libs story:")
    print(final_sentence)

# -------------------------------------
# 🧠 Program Entry Point
# -------------------------------------
if __name__ == '__main__':
    main()

# ------------------------------------------------------
# ✅ End of Program
# ------------------------------------------------------
