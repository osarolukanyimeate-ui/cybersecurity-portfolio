password = input("Enter a password: ")

has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*" for char in password)

if len(password) < 8:
    print("Password is too short.")
elif not has_uppercase:
    print("Password needs at least one uppercase letter.")
elif not has_number:
    print("Password needs at least one number.")
elif not has_special:
    print("Password needs at least one special character.")
else:
    print("Password is strong.")