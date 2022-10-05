from login import login
from useractions import user_actions


def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}

    while True:
        logged_in_user = login(users)
        if logged_in_user != None:
            user_actions(logged_in_user, data[logged_in_user])
            

if __name__ == "__main__":
    main()