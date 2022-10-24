import pyinputplus
import pickle
from os import path

PICKLE_FILE= 'todo_list_database.p'

# Functions:


def create_pickle_file_maybe(filename):
    if not path.exists(filename):
        list_database = dict()
        with open(filename, 'wb') as todo_list_database_file:
            pickle.dump(list_database, todo_list_database_file, protocol=pickle.HIGHEST_PROTOCOL)

def get_database(PICKLE_FILE):
    with open(PICKLE_FILE, 'rb') as todo_list_database_file:
        todo_list_database = pickle.load(todo_list_database_file)
    return todo_list_database



def req_init_menu_selection():
    """prints initial menu. requests int input. returns int"""
    print("1. Create new user")
    print("2. Select existing user")
    print("3. Exit")
    selection = pyinputplus.inputNum(min=1, max=3)
    return int(selection)


create_pickle_file_maybe(PICKLE_FILE)
list_database = get_database(PICKLE_FILE)
init_menu_selection = req_init_menu_selection()

