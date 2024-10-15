def register_user():
    print("Welcome to the Registration System!")

    # Collect user information
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Basic validation
    if username and email and password:
        print("\nRegistration successful!")
        print("User Information:")
        print(f"Username: {username}")
        print(f"Email: {email}")
    else:
        print("Please fill in all fields.")

if __name__ == "__main__":
    register_user()
