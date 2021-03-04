class Door:
    def __init__(self, is_open: bool) -> None:
        self.is_open = is_open

    def push_knob(self):
        msg = "No state change."
        if self.is_open == True:
            self.is_open = False
            msg = "Door is now closed."
        print(msg)

    def pull_knob(self):
        msg = "No state change."
        if self.is_open == False:
            self.is_open = True
            msg = "Door is now open."
        print(msg)
