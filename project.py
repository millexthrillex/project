import pyinputplus
import pickle
from os import path

PICKLE_FILE= 'list_database.p'

# Functions:


def create_pickle_file_maybe(filename):
    if not path.exists(filename):
        list_database = dict()
        with open(filename, 'wb') as handle:
            pickle.dump(list_database, handle, protocol=pickle.HIGHEST_PROTOCOL)



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

