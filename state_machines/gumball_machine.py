import sys, inspect

from machine_states import State


class GumballMachine:
    '''The public interface for the client to change the state of the FSM.'''
    def __init__(self, initial_state='state') -> None:
        # init the current state of the system
        self.current_state = State()
        # init other properties
        self.num_gumballs = None
        self.quarters = None
        # now switch to the state that the client requested
        self.request(initial_state)

    def request(self, requested_change):
        """the client makes a request to transition states, 
        which is delegated to the state
        """
        return self.current_state.handle(requested_change, self)


if __name__ == "__main__":
    # quick test of the gumball machine class
    system = GumballMachine('NoQuarter')  # should throw no error
