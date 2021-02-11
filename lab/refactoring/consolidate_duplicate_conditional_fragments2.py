# By Kami Bigdely-Shamloo
# Consolidate duplicate conditional fragments
# This program changes car's gear according to the car speed. Then it 
# displays the updated gear on the car's front panel.

def change_gear(str_gear):
    print("Gear changed to", str_gear)


def display_gear(str_gear): 
    print("displayed gear:", str_gear)


def process_speed(speed):
    # map the speed bounds to their gears
    bounds = [
        (float("-inf"), 0), (0, 30),
        (30, 50), (50, 90), (90, float("inf"))
    ]
    gears = ['R', '1', '2', '3', '4']
    bounds_to_gears = dict(zip(bounds, gears))
    # define the gear to use
    gear = ''
    for lower_limit, upper_limit in bounds:
        if lower_limit <= speed < upper_limit:
            gear = bounds_to_gears[(lower_limit, upper_limit)]
            break
    # change the gear
    change_gear(gear)
    display_gear(gear)


if __name__ == "__main__":
    process_speed(40)
