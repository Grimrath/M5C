from menu import menu


def login(users):
    while True:
        username = input("    User: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            # A newline for nice formatting's sake.
            print()
            return username
        else:
            options = {"r":"Try again", "q":"Quit"}
            if menu("Invalid username or password", "Option: ", options) == "q":
                # A newline for nice formatting's sake.
                print()
                return None
