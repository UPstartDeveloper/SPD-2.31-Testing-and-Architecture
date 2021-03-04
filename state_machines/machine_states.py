# This module includes all the states the 
# Implementing the UML found here: https://docs.google.com/document/d/1wiD0N9OFVyZz0SASkcnY-cYfIdPfv1SBH9q0ke65rxk/edit

import sys
import inspect
from typing import List


class State:
    """
    An abstraction for what all the states 
    of the gumball machine share in common.
    """
    def __init__(self, name='state', valid_changes=None) -> None:
        self.name = name
        # store a list of the other states we can go to from this one
        if valid_changes is None:
            self.valid_changes = list(self.get_classes().keys())
        else:
            self.valid_changes = valid_changes

    def handle(self, request, gumball_machine):
        """Changes the current state of the 
        gumball_machine to any of its children.
        """
        # get a record of states we can go to 
        concrete_states = self.get_classes()
        # validate the request
        if request in self.valid_changes and request in concrete_states:
            # change the state
            new_state = concrete_states[request]()
            gumball_machine.current_state = new_state

    def get_classes(self):
        """
        At runtime, this utility function will return a dict 
        of all the objects in a module in this repo.

        Parameter:
        module_name(str): where Python can import the module from

        Returns: dict

        Example usage: 
        If we print the output of State().get_classes(), we would get the following:
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
        valid_changes = ['GumballSold', 'NoQuarter']
        super().__init__(name, valid_changes)

    def handle(self, request, gumball_machine):
        '''Changes the system based on the request.'''
        # change the system properties based on the request
        if request == 'GumballSold':
            gumball_machine.num_gumballs -= 1
            gumball_machine.num_quarters += 1
        if request == 'NoQuarter':
            gumball_machine.num_quarters -= 1  # ejects quarter
        # change the system's .current_state property
        return super().handle(request, gumball_machine)
        

class NoQuarter(State):
    def __init__(self, name='no_quarter') -> None:
        valid_changes = ['HasQuarter']
        super().__init__(name, valid_changes)
    
    def handle(self, request, gumball_machine):
        '''Changes the system based on the request.'''
        # change the system properties based on the request
        if request == 'HasQuarter':
            gumball_machine.num_quarters += 1
        # change the system's .current_state property
        return super().handle(request, gumball_machine)


class GumballlSold(State):
    def __init__(self, name='gumball_sold') -> None:
        valid_changes = ['OutOfGumballs', 'NoQuarter']
        super().__init__(name, valid_changes)

    def handle(self, request, gumball_machine):
        '''Changes the system based on the request.'''
        # change the system properties based on the request
        if request == 'OutOfGumballs':
            gumball_machine.num_gumballs = 0
        if request == 'NoQuarter':
            gumball_machine.num_gumballs -= 1
        # change the system's .current_state property
        return super().handle(request, gumball_machine)


class OutOfGumballs(State):
    def __init__(self, name='out_of_gumballs') -> None:
        valid_changes = list()
        super().__init__(name, valid_changes)

    def handle(self, request, gumball_machine):
        '''The gumball machine can no longer take any requests.'''
        print("Sorry, this machine is currently out of order.")


if __name__ == "__main__":
    print(State().get_classes())
