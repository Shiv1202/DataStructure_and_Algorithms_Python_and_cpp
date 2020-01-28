# Python Program for Removing Duplicates from a given String.
"""******************************
1) Without Order.
    a) We can use set() for removing
    duplicate. As we know set is unordered
    collection of unique values.
    b) By Using OrderedDict from Collections
    Modules.
*********************************"""
# Import OrederedDict From Collections.
from collections import OrderedDict

# Function to remove all duplicates
# from string without order.
def remove_dulpi_without_order(s):
    return ''.join(set(s))

# Function to remove all duplicates
# from string with order.
def remove_dulpi_with_order(str):
    return ''.join(OrderedDict.fromkeys(str))

# Main Function.
def main():
    s = "bananaisbanana"
    print("Without Order: " + remove_dulpi_without_order(s))
    print("With Order: " + remove_dulpi_with_order(s))
# Driver code.
if __name__ == "__main__":
    main()