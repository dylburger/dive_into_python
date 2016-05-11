#!/usr/bin/env python3

""" Getting practice with basic Python data types
"""
from data_type_exceptions import NotASetError

""" FUNCTIONS
"""


# Lists
def extend_list(num):
    """ Accepts an integer, num
        Extend a list by a range of numbers, from 0 to num
        Returns the list to pass to the extend method
        If the num passed isn't an integer, a TypeError exception is raised
    """
    return list(range(num))


# Dictionaries
def add_key_to_dict(d, key, val):
    """ Accepts a key and value, to be added to a dictionary
        Returns a copy of the dictionary, with the new key and value added
    """
    # Copy dict
    new_d = d
    new_d[key] = val
    return new_d


# Sets
def get_set_stats(set_a, set_b):
    """ Accepts two sets, a_set and b_set
        Returns interesting statistics about the sets, like the union
        and intersection of the sets, in a single set of print statements
    """
    # A couple of different ways of handling inputs that aren't sets:
    # raise a custom exception...
    if not isinstance(set_a, set):
        raise NotASetError(set_a, "A set needs to be passed as input")
    # Or make an assertion
    assert isinstance(set_b, set), "%s is not a set" % set_b

    # Print summary stats
    print("Set A:", set_a)
    print("Set B:", set_b)
    print("The union of the two sets is: %s" % set_a.union(set_b))
    print("The intersection of the two sets is: %s" %
          set_a.intersection(set_b))


if __name__ == "__main__":
    a = []
    print("Empty list: %s" % a)

    # extend the list
    a.extend(extend_list(10))
    print("New list, after extension: %s" % a)

    try:
        # This will fail, and will raise a TypeError, which we handle below
        a.extend(extend_list(10.5))
    except TypeError:
        print("You failed to pass an integer to the function")

    # convert to tuple
    a_tuple = tuple(a)
    if a_tuple:
        try:
            a_tuple[0] = 'foo'
        except TypeError:
            print("You can't modify a tuple!")

    a_dict = {'foo': 'bar', 'test': 'dictionary'}
    print("Original dictionary: %s" % a_dict)
    a_new_dict = add_key_to_dict(a_dict, 'city', 'San Francisco')
    print("New dictionary: %s" % a_new_dict)

    # Generate some summary stats with good input
    set_a = {1, 2, 3}
    set_b = {1, 3, 5}
    get_set_stats(set_a, set_b)

    # Generate some summary stats with bad input, but handle it
    not_a_set = [1, 2, 3]
    try:
        get_set_stats(not_a_set, set_b)
    except NotASetError as e:
        print("%s. You passed: %s" % (e.message, e.variable))

    # Pass another bad set, but handle the different error that arises
    try:
        get_set_stats(set_a, not_a_set)
    except AssertionError as e:
        print("There was an AssertionError: %s" % e.args[0])
