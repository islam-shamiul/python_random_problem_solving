while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    else:
        print("Please enter your age in decimal formate")

while True:
    print("Enter your password (letters and numbers only):")
    password = input()

    if password.isalnum():
        break
    else:
        print("Passwords can only have letters and numbers.")