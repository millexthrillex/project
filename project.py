import pyinputplus
import pickle
from os import path

PICKLE_FILE= 'todo_list_database.p'

# Functions:


def create_pickle_file_maybe(filename):
    if not path.exists(filename):
        todo_list_database = dict()
        with open(filename, 'wb') as todo_list_database_file:
            pickle.dump(todo_list_database, todo_list_database_file, protocol=pickle.HIGHEST_PROTOCOL)

def get_todo_list_database(PICKLE_FILE):
    with open(PICKLE_FILE, 'rb') as todo_list_database_file:
        todo_list_database = pickle.load(todo_list_database_file)
    return todo_list_database

def req_user_name(todo_list_database):
    while True:
        print("Enter a username:")
        user_name = input()
        user_name = user_name.lower()
        if user_name in todo_list_database:
            print("Name already exists. Try again")
            continue
        return user_name

def req_existing_user(todo_list_database):
    while True:    
        print("names in todo list database")    
        for name in todo_list_database:
            print(name)
        print("enter a name")
        name = input()
        if name in todo_list_database:
            return name
        else:
            print("name not in database. Try again")
    

def req_init_menu_selection():
    """prints initial menu. requests int input. returns int"""
    print("1. Create new user")
    print("2. Select existing user")
    print("3. Exit")
    selection = pyinputplus.inputNum(min=1, max=3)
    return int(selection)


create_pickle_file_maybe(PICKLE_FILE)
todo_list_database = get_todo_list_database(PICKLE_FILE)
init_menu_selection = req_init_menu_selection()

if init_menu_selection == 1:
    user_name = req_user_name(todo_list_database)
    todo_list_database[user_name] = []
    with open(PICKLE_FILE, 'wb') as todo_list_database_file:
        pickle.dump(todo_list_database, todo_list_database_file, protocol=pickle.HIGHEST_PROTOCOL)

elif init_menu_selection == 2:
    user_name = req_existing_user(todo_list_database)
    


