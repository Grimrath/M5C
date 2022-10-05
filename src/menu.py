def menu(title, prompt, options):
    
    print(f"{title}")
    for key, value in options.items():
        print(f"    {key}) {value}")
    
    while True:
        selected = input(prompt)
        if selected in options:
            break

    return selected
