"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

    #show a list of options:
print("Here are your options:")
print("Add or +")
print("Subtract or -")
print("Multiply or *")
print("Divide or /")
print("Square")
print("Cube")
print("Power")
print("Mod or %")
print("Quit")


# repeat forever:
while True:

    print("Type your choice followed by integers separated by a space")
#     read input
    user_prompt = input("> ").lower()
#     tokenize input
    #
    token_list_list = user_prompt.split(" ") #list of 

    for idx, item in enumerate(token_list_list):
        if item.isdigit():
            token_list_list[idx] = int(token_list_list[idx])

#     if the first token is "q":
    if token_list_list[0].startswith("q"):
        break
#         quit
#     else:
#         decide which math function to call based on first token
    elif token_list_list[0].startswith("add") or token_list[0] == "+":
        print(add(token_list[1], token_list[2]))
