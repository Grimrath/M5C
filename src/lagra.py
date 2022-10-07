def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}

    while True:
        print("Welcome to Lagra (TM)", end="\n\n")
        logged_in_user = login(users)
        if logged_in_user != None:
            user_actions(logged_in_user, data[logged_in_user])


def add(prompt, strings):
    strings.append(input(prompt))
    return strings


def login(users):
    while True:
        username = input("    User: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            print()     # A newline for nice formatting's sake.
            return username
        else:
            options = {"r":"Try again", "q":"Quit"}
            print()     # A newline for nice formatting's sake.
            if menu("Invalid username or password", "Option: ", options) == "q":
                print()     # A newline for nice formatting's sake.
                return None


def menu(title, prompt, options):
    # Printing is an allowed side-effect
    print(f"{title}", end="\n\n")
    for key, value in options.items():
        print(f"    {key}) {value}")
    print() # A newline for nice formatting's sake.
    while True:
        selected = input(prompt)
        if selected in options:
            return selected


def user_actions(user, items):
    print(f"Welcome, {user}!")
    view("These are your items", items)

    options = {"a":"Add an item", "v":"View items", "l":"Log out"}

    logged_in = True
    while logged_in:
        selection = menu("Select an action", "Option: ", options)
        if selection == "a":
            print()     # A newline for nice formatting's sake.
            add("Add an item: ", items)
        elif selection == "v":
            print()     # A newline for nice formatting's sake.
            view("These are your items", items)
        elif selection == "l":
            logged_in = False
            print()     # A newline for nice formatting's sake.
            return items


def view(description, strings):
    # Printing is an allowed side effect
    print(description)
    for i, string in enumerate(strings):
        print(f"    {i}) {string}")
    print()     # A newline for nice formatting's sake.
    return



if __name__ == "__main__":
    main()