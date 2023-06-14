#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    different_set = set()
    
    # Iterate over each element in set_1
    for element in set_1:
        # If the element is not present in set_2, add it to the different_set
        if element not in set_2:
            different_set.add(element)
    
    # Iterate over each element in set_2
    for element in set_2:
        # If the element is not present in set_1, add it to the different_set
        if element not in set_1:
            different_set.add(element)
    
    return different_set
