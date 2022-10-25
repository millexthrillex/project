import pyinputplus
import pickle
from os import path
from pprint import pprint

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

def req_todo_menu_selection():
    print("1. Print list")
    print("2. Add item to list")
    print("3. Remove item from list")
    selection = pyinputplus.inputNum(min=1, max=4)
    return int(selection)

def print_user_names_todo_list(todo_list_database, user_name):
    user_names_todo_list = todo_list_database[user_name]
    pprint(user_names_todo_list)
    print("length of list is:", len(user_names_todo_list))

def get_todo_list_item():
    print("enter a todo list item to be added:")
    todo_list_item = input()
    return todo_list_item

def get_todo_list_item_index(todo_list_database, user_name):
    users_todo_list = todo_list_database[user_name}
    for index, todo_list_item in enumerate(users_todo_list):
        print(f"[index}. todo_list_item")
    selection = pyinputplus.inputNum(min=1, max=4)
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

todo_menu_selection = req_todo_menu_selection()

if todo_menu_selection == 1:
    print_user_names_todo_list(todo_list_database, user_name)
elif todo_menu_selection == 2:
    todo_list_item = get_todo_list_item()
    todo_list_database[user_name].append(todo_list_item)
    with open(PICKLE_FILE, 'wb') as todo_list_database_file:
        pickle.dump(todo_list_database, todo_list_database_file, protocol=pickle.HIGHEST_PROTOCOL)
    print("item added")
elif todo_menu_selection == 3:
    if len(todo_list_database[user_name]) == 0
        print("todo list has a length of 0. Select another menu option")
    todo_list_item_index = get_todo_list_item_index(todo_list_database, user_name)

