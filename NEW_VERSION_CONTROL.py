def password_encoder(password):
    # Convert each digit to an integer, shift it up by 3, and convert it back to a string
    encoded_password = ''.join(str((int(digit) + 3) % 10) for digit in password)

    return encoded_password


original_password = ''
encoded_password = ''


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = password_encoder(original_password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}")
        elif option == 3:
            break
