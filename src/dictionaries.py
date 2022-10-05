users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

print("Användare:", end="\n\n")
for key in users:
    print(f"    {key}")
    

print("Användare och lösenord:", end="\n\n")
for key, value in users.items():
    print(f"    {key}) {value}")
    

print("Användare och deras data:", end="\n\n")

for key,value in data.items():
    print(f"    {key}) {value}")
    

user = input("Slå upp användare: ")
print()
if user in users:
    print(f"Data lagrat för {user}: {data[user]}")
    print()
else:
    print(f"User '{user}' not found.")
    print()