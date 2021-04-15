# Give a list of names
# make random pairs 
# Save the list 

import random 
import pickle
import os
from datetime import date


def open_dat():
    """This function opens a .dat file and reads the saved list from it."""
    # Current Working Directory
    cwd = os.getcwd()
    try:
        previous_list = pickle.load(open(cwd + "\\savedList.dat", "rb"))
        return previous_list
    except FileNotFoundError:
        return []

def validate_pair(pair_to_validate):
    """This function checks if the pair has been used in the previous list of pairs."""
    previous: list = open_dat()
    if previous:
        # dim_1: dimension_1
        for dim_1 in previous:
            if pair_to_validate in dim_1 or pair_to_validate.reverse() in dim_1:
                return False
        return True
    else:
        return True

def get_pairs():
    """This function is used to get the list of names that will be used for pairing."""

    print("How many pairs would you want to make?\n")

    while True:
        try:
            inputs = input()
            inputs = int(inputs) * 2
            break
        except ValueError:
            print("Please enter a valid number.")
            continue
    
    print(f"\nYou are going to pair {inputs} names.")

    list_of_names = []
    for _ in range(inputs):
        if list_of_names:
            while len(list_of_names) != inputs:
                print("Please enter a name you would like to pair.\n")
                in_name = input()
                if in_name in list_of_names:
                    print("You have entered a name that is already in the list.\nPlease enter unique names.\n")
                    continue
                else:
                    list_of_names.append(in_name)
                    if len(list_of_names) == inputs:
                        break
        else:
            print("Please enter a name you would like to pair.\n")
            in_name = input()
            list_of_names.append(in_name)
    
    print("\nThis is the list of names to be paired.")
    print(f"{list_of_names}\n")
    
    return list_of_names


def randomize_names(names_list):
    """This function is used to create the random pairs."""
    randomized = []
    for x in range(int(len(names_list)/2)):
        pair = random.sample(names_list, 2)
        if validate_pair(pair):
            pass
        else:
            continue
        
        duo = pair.copy()
        print(f"Pair:   {pair}\n")
        randomized.append(duo)
        first = pair.pop()
        second = pair.pop()

        names_list.remove(first)
        names_list.remove(second)

    print("This is the randomized list:")
    print(randomized)
    return randomized


def make_text(list_to_text):
    """This function saves the list as a text file"""
    today = date.today()

    try:
        with open("newNames.txt", "a") as text:
            text.writelines("\n")
            text.writelines(f"{today}\n")
            text.writelines(f"List added: {list_to_text}\n")
    except:
        print("\nThere was an issue while saving the list to a text file.\n")

    print("\nThe text file was created successfully\n")


def save_to_dat(list_to_be_saved):
    """This function creates a dat file and saves the list of names."""
    # Current Working Directory
    cwd = os.getcwd()
    pickle.dump(list_to_be_saved, open(cwd + "\\savedList.dat", "wb"))
    print("The list has been saved to: savedList.dat\n")


def menu():
    """This function has the functions that are used when running the program."""
    variable = get_pairs()
    names = randomize_names(variable)
    make_text(names)
    save_to_dat(names)

# This section runs the code.
if __name__ == "__main__":
    while True:
        print("Welcome to the Pairing System\n")
        menu()
        print("Thank you for using the pairing system.\n")
        print("Would you like to\n1.)Use the paring system again\n2.)Exit")
        choice = input()
        if choice.lower() in ["1", "1.", "1.)", "one"]:
            continue
        else:
            break
    print("\nThank you for using The Pairing System\n")
    input()