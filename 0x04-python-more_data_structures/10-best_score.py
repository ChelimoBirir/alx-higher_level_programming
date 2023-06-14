#!/usr/bin/python3
def best_score(a_dictionary):
    # Initialize variables to keep track of the maximum score and corresponding key
    max_score = float('-inf')
    max_key = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the current value is greater than the maximum score
        if value > max_score:
            # Update the maximum score and corresponding key
            max_score = value
            max_key = key

    return max_key
