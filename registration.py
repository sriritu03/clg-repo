def register_user(username, email, password):
    # Simulated registration process
    if username and email and password:
        print("Registration successful!")
        print("User Information:")
        print(f"Username: {username}")
        print(f"Email: {email}")
    else:
        print("Please provide all required fields.")

if __name__ == "__main__":
    # Hard-coded user data
    username = "john_doe"
    email = "john@example.com"
    password = "securepassword"

    # Register the user
    register_user(username, email, password)

