#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dict = {}

    # Iterate over the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply the value by 2 and add it to the new dictionary
        multiplied_dict[key] = value * 2

    return multiplied_dict
