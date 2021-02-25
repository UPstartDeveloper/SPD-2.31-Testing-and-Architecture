# test_exercise_4.py

import pytest
import .exercise_4_function as e4


@pytest.fixture
def average_input():
    return "|update| the positron location \
        in the particle accelerator is x:21.432"


@pytest.fixture
def null_input():
    """For whatever reason the device is not inputting any value."""
    return None


@pytest.fixture
def error_input():
    """Something went wrong with the machine, so the log reports an error."""
    return "|error| numerical calculations could not converge."


def test_extract_position_average_case(average_input):
    """Reads in a log from the device, and returns
    the location of the positron (if mentioned)."""
    # Expected Input - contains 'x:
    assert e4.extract_position(average_input) == "21.432"


def test_extract_position_null_case(null_input):
    """Reads in a log that's None"""
    # NoneType Input
    assert e4.extract_position(null_input) == None


def test_extract_position_null_case(error_input):
    """Reads in a log when the machine is broken"""
    # Error Input - 'debug' or 'error'
    assert e4.extract_position(error_input) == None
    