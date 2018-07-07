#!/usr/local/bin/python3

import re


def wildcard_combinations(data: str):
    if not isinstance(data, str) or not re.match(r'[01xX]+', data):
        raise ValueError('Please enter a string containing only 1, 0 or X')
    result = ['']
    for x in data:
        if x == '1' or x == '0':
            for i in range(len(result)):
                result[i] += x
        else:
            for i in range(len(result)):
                result.append(result[i] + '0')
                result[i] += '1'
    print('\n'.join(result))


# Testing
if __name__ == '__main__':
    import sys

    data = sys.argv[1]
    wildcard_combinations(data)
