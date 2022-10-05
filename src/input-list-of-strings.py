def add(prompt, strings):
    strings.append(input(prompt))
    return strings


def view(description, strings):
    print(description + "\n")
    for i, string in enumerate(strings):
        print(f"    {i}) {string}")
    return


n = 5
list_of_stuff = []

for _ in range(n):
    add("lägg till en sträng: ", list_of_stuff)
    
view("du har matat in", list_of_stuff)
