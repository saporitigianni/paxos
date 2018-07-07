#!/usr/local/bin/python3

"""
Script to print out every possible combination resulting from replacing a
wildcard (X) for both a 1 and a 0 in a string containing 0s, 1s and Xs

############################### Time Complexity ###############################
Best case scenario will be O(n) if the string does not contain any wildcards
since the script will go through every character only once

Worst case scenario will be O(2**n) if the string contains only wildcards
since every element will be subsequently appended with both a '0' and a '1'
which will double the number of elements for each item on the string

############################## Space Complexity ###############################
Best case scenario will be O(1) since only one string will be returned for the
best case time complexity mentioned above

Worst case scenario will be O(2**n) since at most 2**n elements will be
returned for the worst case time complexity mentioned above
"""
import re


def wildcard_combinations(in_string: str):
    """
    Prints every possible combination resulting from replacing a wildcard (X)
    for both a 1 and a 0 in a string containing 0s, 1s and Xs

    Input:
        in_string: string containing only 1, 0, or X characters

    Output:
        None
    """
    if not isinstance(in_string, str) or re.search(r'[^01X]', in_string):
        raise ValueError('Please enter a string containing only 1, 0 or X.')

    # Recursive helper using generators
    def wildcard_helper(word):
        if len(word) == 1:
            if word != 'X':
                yield word
            else:
                yield '0'
                yield '1'
        else:
            temp = word[0]
            if temp != 'X':
                for res in wildcard_helper(word[1:]):
                    yield temp + res
            else:
                for res in wildcard_helper(word[1:]):
                    yield '0' + res
                    yield '1' + res

    # Print each value as retrieved from generator to avoid hanging for many Xs
    for x in wildcard_helper(in_string):
        print(x)


# If ran from the terminal
if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        raise ValueError('Missing argument. Please enter a string as the first'
                         ' argument')

    data = sys.argv[1]
    wildcard_combinations(data)
