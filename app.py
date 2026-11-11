from datetime import datetime 
import json
import os

number_to_shelter_info = {
    1:"shelter_name",
    2:"leader",
    3:"survivors",
    4:"food",
    5:"water",
    6:"baricade_health",
    7:"radio_working"
}

shelter_info = {}
with open("shelter.json", "r") as file:
        shelter_info = json.load(file)

def get_time():
    """gets the time"""
    current_time = datetime.now() 
    timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")
    return timestamp

def clear():
    """clears screen"""
    os.system('cls')

def pause():
    """pauses the program until user hits enter"""
    user = input("Press enter to continue... ")

def invalid_input():
    """tells the user if they entered an invalid input"""
    clear()
    print("invalid input")
    pause()

def get_valid_input_int(min="", max="", prompt="No prompt entered: ", menu=""):
    """Makes sure the user enters a valid integer"""
    while True:
        clear()
        if menu != "":
            print(menu)
        user = input(prompt).strip()
        if user.isdigit():
            user = int(user)
            if min != "" and max != "":
                return user if user >= min and user <= max else invalid_input()
            elif min != "" and max == "":
                return user if user >= min else invalid_input()
            elif min == "" and max != "":
                return user if user <= max else invalid_input()
            else:
                return user
        else:
            invalid_input()

def get_valid_input_str(prompt="No prompt entered: ", menu=""):
    """Makes sure the user enters a valid string"""
    while True:
        clear()
        if menu != "":
            print(menu)
        user = input(prompt).strip()
        if user.isdigit():
            invalid_input()
        else:
            return user

def get_valid_input_boolean(prompt="No prompt entered: ", menu=""):
    """Makes sure the user enters a valid boolean"""
    while True:
        clear()
        if menu != "":
            print(menu)
        user = input(prompt).strip()
        if user.lower() == "true" or user == "1":
            return True
        elif user.lower() == "false" or user == "2":
            return False
        else:
            invalid_input()

def get_shelter_info(shelter_info, x):
    """Gathers all the shelter information and prints it to show the user"""
    clear()
    if x == True:
        print(f"""Shelter name: {shelter_info["shelter_name"]}
leader: {shelter_info["leader"]}
survivors: {shelter_info["survivors"]}
food: {shelter_info["food"]}
water: {shelter_info["water"]}
baricade health: {shelter_info["barricade_health"]}
Radio working: {shelter_info["radio_working"]}
""")
    pause()
    return shelter_info

def change_shelter_info(shelter_info: dict):
    """Lets the user change any of the shelter's information"""
    clear()
    menu = f"""1. Shelter name: {shelter_info["shelter_name"]}
2. leader: {shelter_info["leader"]}
3. survivors: {shelter_info["survivors"]}
4. food: {shelter_info["food"]}
5. water: {shelter_info["water"]}
6. baricade health: {shelter_info["barricade_health"]}
7. Radio working: {shelter_info["radio_working"]}
"""
    user = get_valid_input_int(1, 7, "Enter what value you'd like to change: ", menu)
    if user > 2 and user < 7:
        user = number_to_shelter_info[user]
        user2 = get_valid_input_int(prompt="Enter a valid input between 0-100: ")
        shelter_info[user] = user2
    elif user == 2:
        user2 = get_valid_input_str(prompt="Enter a valid leader name: ")
        shelter_info[user] = user2
    elif user == 1:
        user2 = get_valid_input_str(prompt="Enter a valid shelter name: ")
        shelter_info[user] = user2
    else:
        user2 = get_valid_input_boolean(prompt="Enter a valid input: ", menu="1. working radio\n2. broken radio\n")
        shelter_info[user] = user2
        print("Radio is now working") if shelter_info[user] == True else print("Radio is not working now")
        pause()
    return user, user2

def log_change(value, change):
    """logs any change the user makes"""
    clear()
    time = get_time()
    with open("shelter.log", "a") as file:
        file.write(f"{time}: {value} was changed to {change}\n")
        print("change logged successfully")
        pause()

def read_change_log():
    """reads a file with all the changes the user made"""
    clear()
    try:
        with open("shelter.log", "r") as file:
            shelter_logs = file.read()

        if shelter_logs.strip():
            print(shelter_logs)
        else:
            print("The reading journal is empty.")
    except FileNotFoundError:
        print("No reading journal entries have been saved yet.")

def clear_change_log():
    """clears the file with all the changes the user made"""
    with open("shelter.log", "w") as file:
        file.write("",end="")

def main_menu(dict: dict):
    """runs the main menu which is more so the main function"""
    while True:
        clear()
        print("""Zombie Shelter Manager 
1. View shelter information 
2. Change a shelter value 
3. View change log 
4. Quit 
""")
        user = input("Enter a valid input: ").strip()
        if user == "4" or user.lower() == "q":
            break
        elif user == "1":
            get_shelter_info(dict, True)
        elif user == "2":
            shelter_change, user_change = change_shelter_info(dict)
            log_change(shelter_change, user_change)
        elif user == "3":
            user = input("Enter 1 to read change log or 2 to clear it: ")
            if user == "1":
                read_change_log()
                pause()
            elif user == "2":
                clear_change_log()
                pause()

main_menu(shelter_info)