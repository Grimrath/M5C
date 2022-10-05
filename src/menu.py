from view import view
from add import add


def menu(title, prompt, options):
    
    print(f"{title}")
    for key, value in options.items():
        print(f"    {key}) {value}")
    
    while True:
        selected = input(prompt)
        if selected in options:
            break

    return selected
    #print(f"You selected option {selected}) {options[selected]}")

options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"You selected action {opt1}) {options1[opt1]}")
print()
options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")