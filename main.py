from password_vault import Storage, Password, generate_password

# User interface
print('''
Welcome to the password storage system.

1. Create and store a password.
2. Add a password.
3. Retrieve a password(Full name).
4. Retrieve a password(Short name).

Press 'q' to quit.
''')

# Initialize password storage object
password_storage = Storage()

# Continuously prompt user for input until they quit the program
while True:
    user_input = input("Enter your selection: ")

    if user_input == "q":
        print("Exiting the program...")
        break

    elif user_input == "1":
        platform_name = input("Enter platform name: ")
        short_name = input("Enter a short name: ")
        #password_length = int(input("Enter the password length: "))
        generated_password = generate_password()
        password = generated_password

        new_password = Password(platform_name, short_name, password)
        print("Adding password...")
        password_storage.add_password(new_password)
        print("Password added successfully.")

    elif user_input == "2":
        platform_name = input("Enter platform name: ")
        short_name = input("Enter a short name: ")
        password = input("Enter the password: ")

        new_password = Password(platform_name, short_name, password)
        print("Adding password...")
        password_storage.add_password(new_password)
        print("Password added successfully.")

    elif user_input == "3":
        platform_name = input("Enter the platform name: ")
        password_storage.search_password_full(platform_name)

    elif user_input == "4":
        short_name = input("Enter the platform name: ")
        password_storage.search_password_short(short_name)
    else:
        print("Invalid selection.")
