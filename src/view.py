def view(description, strings):
    print(description)
    for i, string in enumerate(strings):
        print(f"    {i}) {string}")
    print()     # A newline for nice formatting's sake.
    return
