# Written by Krzysztof Hodun album no: 79114
def encrypt_string():
    print("Encryption:\n")
    the_string = input("Would you kindly type something in here: ").upper()
    print("Provided input: " + the_string.lower())

    letters = {"Y": "E",
               "A": "Y",
               "E": "I",
               "I": "O",
               "O": "A"}
    output = ""
    for letter in the_string:
        if letter in letters:
            output += letters[letter]
        else:
            output += letter

    print("The encoded message is: " + output.lower() + "\n")


def decrypt_string():
    print("Decryption:\n")
    the_string = input("Would you kindly type something in here: ").upper()
    print("Provided input: " + the_string.lower())

    letters = {"Y": "A",
               "A": "O",
               "E": "Y",
               "I": "E",
               "O": "I"}
    output = ""
    for letter in the_string:
        if letter in letters:
            output += letters[letter]
        else:
            output += letter

    print("The decoded message is: " + output.lower() + "\n")
