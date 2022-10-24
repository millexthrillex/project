##
import pyinputplus
import json

def req_init_menu_selection():
        """prints initial menu. requests int input. returns int"""
        print("1. Select existing user")
        print("2. create new user")
        print("Enter a number:")
        selection = pyinputplus.inputNum(min=1, max=2)
        return int(selection)

def req_new_user():
        print("Enter a username:")
        user_name = input()
        return user_name

def add_new_user(user_name):
        try:
                df = pd.read_json('data.json')
        except (FileNotFoundError, ValueError):
                init_user = {user_name: [[]]}
                df = pd.DataFrame(init_user)
                df.to_json('data.json')
        return df

while True:
        init_menu_selection = req_init_menu_selection()
        if init_menu_selection == 1:
                user_name = req_new_user()
                add_new_user(user_name)
        elif init_menu_selection == 2:

