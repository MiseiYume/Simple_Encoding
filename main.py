# Written by Krzysztof Hodun album no: 79114
import encryption_operations
import sys


def menu():
    i = 1
    while (i != 0):
        try:
            option = input("Plz gib number:\n\n1. Encrypt.\n"
                           "2. Decrypt.\n0. End.\n")
            option = int(option)
            if (option == 1):
                encryption_operations.encrypt_string()
            elif (option == 2):
                encryption_operations.decrypt_string()
            elif (option == 0):
                print("Leaving...\nGoodbye cruel world.")
                sys.exit()
            else:
                print("Unknown command.\n")
        except ValueError:
            print("OOPSIE WOOPSIE!! Uwu We made a fucky wucky!!"
                  "A wittle fucko boingo! The code monkeys at "
                  "our headquarters are working VEWY HAWD to "
                  "fix this!\n")


menu()
