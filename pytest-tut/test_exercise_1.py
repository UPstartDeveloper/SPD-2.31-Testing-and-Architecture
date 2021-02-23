# test_exercise_1.py

import math

def get_average(li):
    if len(li) == 0:
        return float('NaN')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean


def test_get_average_expected_inputs():
    # all pos
    assert get_average([2, 2, 2, 2]) == 2
    # pos integers and floats
    assert get_average([2.5, 2, 2.5, 2]) == 2.25
    # pos floats
    assert get_average([3.33, 9.99]) == 6.66
    # pos and neg ints
    assert get_average([2, 2, 2, -22]) == -4
    # pos, neg, ints, and floating points
    assert get_average([4.78, -7, 2.22, -22]) == -5.5
    assert math.isclose(get_average([10.1, 0.01, 0.1]), 3.4033333333)


def test_get_average_empty_list():
    assert math.isnan(get_average([]))