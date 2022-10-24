##
import pyinputplus


def req_init_menu_response():
        """prints initial menu. requests int input. returns int"""
        print("Select an option:")
        print("1. Select from existing user list")
        print("2. create new user")
        selection = pyinputplus.inputNum(min=1, max=2)
        return int(selection)

def create_new_user():
        pass

def main():
        init_menu_selection = req_init_menu_response()
        pass

if __name__ == '__main__':
	main()
