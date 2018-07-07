#!/usr/local/bin/python3

from wildcard_combinations import wildcard_combinations


# Testing
test_cases = ['0', '1', 'X', '1010101', '10X10X0', 'XXXX']
for case in test_cases:
    print('Testing input: {}'.format(case))
    wildcard_combinations(case)
