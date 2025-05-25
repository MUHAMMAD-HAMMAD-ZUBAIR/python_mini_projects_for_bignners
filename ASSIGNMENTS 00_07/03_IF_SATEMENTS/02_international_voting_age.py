# ------------------------------------------------------
# 👨‍💻 Author: Muhammad Hammad Zubair
# 📅 Date: May 2025
# 📘 Lesson: Conditional Statements – Voting Eligibility
# ------------------------------------------------------

# Voting age constants for fictional countries
PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Prompt user to enter their age
    user_age = int(input("👤 How old are you? "))

    # Check voting eligibility for Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"✅ You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"❌ You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")

    # Check voting eligibility for Stanlau
    if user_age >= STANLAU_AGE:
        print(f"✅ You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"❌ You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")

    # Check voting eligibility for Mayengua
    if user_age >= MAYENGUA_AGE:
        print(f"✅ You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"❌ You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == '__main__':
    main()
