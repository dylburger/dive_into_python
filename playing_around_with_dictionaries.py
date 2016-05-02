#!/usr/bin/python

""" Playing around with basic dictionary functionality]
"""
import sys


def main():

    # Instantiate our dictionary
    d = {"server": "dylburger.com", "db": "foo"}
    # Print the contents of our dict
    print d
    # Reference a specific element and print
    print "The value of the server key in our dictionary is: %s" % (d["server"])

    # Add a new element to our dict and print
    print "Adding new element 'bar' to dictionary"
    d["bar"] = "baz"
    print "The value of the bar key in our dictionary is: %s" %(d["bar"])


if __name__ == "__main__":
    main()
