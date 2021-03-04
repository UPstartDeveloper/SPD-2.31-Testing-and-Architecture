# This module includes all the states the 
# Implementing the UML found here: https://docs.google.com/document/d/1wiD0N9OFVyZz0SASkcnY-cYfIdPfv1SBH9q0ke65rxk/edit

import sys
import inspect


class State:
    """
    An abstraction for what all the states 
    of the gumball machine share in common.
    """
    def __init__(self, name='state') -> None:
        self.name = name

    def handle(self, request, context):
        '''Changes the current state of the context to any of its children.'''
        # get a record of states we can go to 
        concrete_states = self.get_classes()
        # validate that request
        if request in concrete_states:
            # change the state
            new_state = concrete_states[request]()
            context.current_state = new_state

    def get_classes(self):
        """
        At runtime, this utility function will return a dict 
        of all the objects in a module in this repo.

        Parameter:
        module_name(str): where Python can import the module from

        Returns: dict

        Example usage:
        If I call print_classes() as is, I would get the following:
        {
            'GumballlSold': <class 'machine_states.GumballlSold'>
            'HasQuarter': <class 'machine_states.HasQuarter'>
            'NoQuarter': <class 'machine_states.NoQuarter'>
            'OutOfGumballs': <class 'machine_states.OutOfGumballs'>
            'State': <class 'machine_states.State'>
        }

        More Info: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
        """
        class_names = list()
        class_objects = list()
        for name, object in inspect.getmembers(__import__(__name__)):
            # validate this is actually a class
            if inspect.isclass(object):
                class_names.append(name)
                class_objects.append(object)
        # make and return the dictionary
        return dict(zip(class_names, class_objects))


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


if __name__ == "__main__":
    print(State().get_classes())