def main():
    # 🔢 Ask the user for a number and convert it to float
    num: float = float(input("Type a number to see its square: "))

    # 📐 Calculate the square of the number (num ** 2)
    square = num ** 2

    # 🖨️ Print the result with emojis for fun
    print(f"{num} squared is {square} ✖️✨")


if __name__ == '__main__':
    main()
