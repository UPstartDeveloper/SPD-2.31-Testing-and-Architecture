# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def get_distance(xc1=4, xc2=4.25, yc1=53, yc2=-5.35):
    # Calculate the distance between the two circle
    return math.sqrt((xc1 - xc2) ** 2 + (yc1 - yc2) ** 2)


print("distance", get_distance())


# *** somewhere else in your program ***
def get_length(xa=-36, ya=97, xb=0.34, yb=0.91):
    # calcualte the length of vector AB vector which is a vector between A and B points.
    return math.sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb))


print("length", get_length())
