def login(username, password):
    # Hard-coded credentials
    correct_username = "john_doe"
    correct_password = "securepassword"

    # Check if the provided credentials match
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")

if __name__ == "__main__":
    # Hard-coded login credentials
    username = "john_doe"
    password = "securepassword"

    # Attempt to log in
    login(username, password)
