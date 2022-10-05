from add import add
from view import view
from menu import menu


def user_actions(user, items):
    print(f"Welcome, {user}!")
    view("These are your items", items)

    options = {"a":"Add an item", "v":"View items", "l":"Log out"}

    logged_in = True
    while logged_in:
        selection = menu("Select an action", "Option: ", options)
        if selection == "a":
            print()
            add("Add an item: ", items)
        elif selection == "v":
            print()
            view("These are your items", items)
        elif selection == "l":
            logged_in = False
            print()
            return items

    
