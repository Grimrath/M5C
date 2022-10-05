def menu(title, prompt, options):
    
    print(f"{title}")
    for key, value in options.items():
        print(f"    {key}) {value}")
    
    while True:
        selected = input(prompt)
        if selected in options:
            break

    return selected

def login(users):
    while True:
        username = input("    User: ")
        password = input("Password: ")
        if username in users and users[username] == password:
            return username
        else:
            options = {"r":"Try again", "q":"Quit"}
            if menu("Invalid username or password", "Option: ", options) == "q":
                return
            
if __name__ == "__main__":
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    user = login(users)