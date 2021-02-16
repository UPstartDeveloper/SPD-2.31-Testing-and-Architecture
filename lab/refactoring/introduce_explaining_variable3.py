# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05


def get_cooking_state(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT


def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cooked_state = get_cooking_state(time, temperature, pressure)
    if desired_state == "well-done" and cooked_state >= WELL_DONE:
        return True
    if desired_state == "medium" and cooked_state >= MEDIUM:
        return True
    return False
