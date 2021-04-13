# Give a list of names
# make random pairs 
# Save the list 

import random 
import pickle
import os
from datetime import date


def get_pairs():
    """This function is used to get the list of names that will be used for pairing."""

    def validate_pair(pair_to_validate):
        """This function checks if the pair has been used in the previous list of pairs."""
        pass

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
    randomized = []
    for x in range(int(len(names_list)/2)):
        pair = random.sample(names_list, 2)
        
        duo = pair.copy()
        print(f"Pair:   {pair}\n")
        randomized.append(duo)
        first = pair.pop()
        second = pair.pop()

        names_list.remove(first)
        names_list.remove(second)

    print("This is the randomized list.")
    print(randomized)
    return randomized


def make_text(list_to_text):
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
    """This function creates"""
    # Current Working Directory
    cwd = os.getcwd()
    pickle.dump(list_to_be_saved, open("savedList.dat", "wb"))


def menu():
    """This function will have the menu that is seen when the program is started."""
    variable = get_pairs()
    names = randomize_names(variable)
    make_text(names)
