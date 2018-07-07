#!/usr/local/bin/python3

"""
Script to print out the optimal way to spend a gifcard when buying two items so
that the remaining balance is minimized

############################### Time Complexity ###############################
Best case scenario will be O(1) if the first 2 items on the prices.txt file
match the amount to be spent since the script will only look at those first
two line and exit

Worst case scenario will be O(n * log(n)) if no two items fully spend the
giftcard or if the last two items on the list spend the full amount since the
script will perform a binary search on every item in the prices.txt file

############################## Space Complexity ###############################
Best case scenario will be O(1) since only the first two items in the file will
be read and stored temporarily for comparison for the best case time complexity
mentioned above

Worst case scenario will be O(n) since at most all of the items in the file
will be stored temporarily for comparison for the worst case time complexity
mentioned above
"""


def giftcard_spending(file_name, balance):
    """
    Find optimal way to buy 2 items and spend as much of a gift card as possible

    Input:
        file_name: string, assuming file is local, name of the file with list
            of sorted prices
        balance: string or int denoting the balance of the gift card

    Output:
        None
    """
    if not isinstance(file_name, str):
        raise ValueError('Please enter a string for the filename.')
    try:
        balance = int(balance)
    except ValueError:
        raise ValueError('Please enter a numeric/integer string or int for the'
                         ' balance')

    prices = []  # Keeps track of all items from the provided file, sorted

    def parse(pair):
        """Format each line of input to a tuple such as (identifier, value)"""
        return pair[0].strip(), int(pair[1].strip())

    def bin_search(arr, x):
        """
        Find largest value less than or equal to x in arr and return its index.
        Returns -1 if no item in arr meets the criteria.
        """
        lo = 0
        hi = len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if x < arr[mid][1]:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1

    with open(file_name, 'r') as file:
        # Initialize the search with the first 2 items from the file
        prices.append(parse(file.readline().split(',')))
        prices.append(parse(file.readline().split(',')))
        diff = balance - prices[0][1] - prices[1][1]

        # Check if the first 2 items are already bigger than the balance
        if diff < 0:
            print("Not possible")
            return

        result = [0, 1]  # Initialize array to keep track of best result
        line = file.readline()
        while line:
            temp = parse(line.split(','))
            # Calculate remaining balance of gift card given the current line
            # and perform binary search on list of prices
            remaining = balance - temp[1]
            optimal_index = bin_search(prices, remaining)
            # If no item can be paired with the current value exit loop
            if optimal_index < 0:
                break

            prices.append(temp)
            # Evaluate the current possible solution which will be the latest
            # item added to 'prices' and the optimal index found above
            candidate = [optimal_index, len(prices) - 1]
            bal = balance - (prices[candidate[0]][1]
                             + prices[candidate[1]][1])
            # If two items that add up to the balance of the gift card
            # are found then exit loop and print those
            if bal == 0:
                result = candidate.copy()
                break
            # If gift card was not fully spent then record opportunity and
            # continue looking
            if bal < diff:
                diff = bal
                result = candidate.copy()
            line = file.readline()

        print('{}, {}'.format('{} {}'.format(*prices[result[0]]),
                              '{} {}'.format(*prices[result[1]])))
        return


# If ran from the terminal
if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 2:
        raise ValueError('Missing arguments. Please enter a filename and a '
                         'balance to spend')

    file = sys.argv[1]
    bal = sys.argv[2]
    giftcard_spending(file, bal)
