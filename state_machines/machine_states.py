# This module includes all the states the 
# Implementing the UML found here: https://docs.google.com/document/d/1wiD0N9OFVyZz0SASkcnY-cYfIdPfv1SBH9q0ke65rxk/edit

import sys

class State:
    """
    An abstraction for what all the states 
    of the gumball machine share in common.
    """
    def __init__(self, name) -> None:
        pass

    def handle(self, context):
        pass


"""CONCRETE STATES"""


class HasQuarter(State):
    def __init__(self, name='has_quarter') -> None:
        super().__init__(name)


class NoQuarter(State):
    def __init__(self, name='no_quarter') -> None:
        super().__init__(name)


class GumballlSold(State):
    def __init__(self, name='gumball_sold') -> None:
        super().__init__(name)


class OutOfGumballs(State):
    def __init__(self, name='out_of_gumballs') -> None:
        super().__init__(name)
