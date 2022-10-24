##
import pyinputplus


def req_menu1_response():
        print("Select an option:")
        print("1. Select from existing user list")
        print("2. create new user")
        response = pyinputplus.inputNum()
        return response
        

def main():
        req_menu1_response()
        pass

if __name__ == '__main__':
	main()
