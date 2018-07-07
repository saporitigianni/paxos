#!/usr/local/bin/python3

from giftcard_spending import giftcard_spending

# Testing
test_cases = ['2500', '2300', '10000', '1100', '900000', '900500', '1800000', '1810000']
for case in test_cases:
    giftcard_spending('prices.txt', case)
