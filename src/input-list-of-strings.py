def add(prompt, strings):
    strings.append(input(prompt))
    return strings


def view(description, strings):
    print(description)
    for i, string in enumerate(strings):
        print(f"    {i + 1}) {string}")
    return


n = 5
list_of_stuff = []

print(f"n = {n}")
for _ in range(n):
    add("lägg till en sträng: ", list_of_stuff)
    
view(f"Du har matat in följande {n} strängar:", list_of_stuff)
