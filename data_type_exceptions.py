""" Classes to handle custom data type exceptions
"""


class Error(Exception):
    """ Base class for our exceptions
    """
    pass


class NotASetError(Error):
    """ Exception raised for input error, when the value required isn't a set

    Attributes:
        variable: The offending variable
        message: A verbose message directing the user to fix the issue
    """
    def __init__(self, variable, message):
        self.variable = variable
        self.message = message
