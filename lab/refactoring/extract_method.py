"""Written by Kamran Bigdely
Example for Compose Methods: Extract Method."""
import math


def get_grades(n_students):
    """Prompt the user to input the grades for n students.

    Args:
        n_students: int. Number of grades to input.

    Returns: a list of floating point values
    """
    grade_list = []
    # Get the inputs from the user
    for _ in range(n_students):
        grade_list.append(int(input("Enter a number: ")))
    return grade_list


def compute_stats(grade_list):
    """Compute and return the mean and standard deviation of the grades.

    Args:
        grade_list: List[float]. A list of numerical grade values.

    Returns: a Tuple[float] of the mean and standard deviation.
    """
    # Calculate the mean and standard deviation of the grades
    mean = sum(grade_list) / len(grade_list)
    sd = 0  # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return mean, sd


def print_stat(n_students):
    """Display the mean and standard deviation for the class.

    Args:
        n_students: int. The number of students in the class.

    Returns: None.
    """
    # get the grades
    grade_list = get_grades(n_students)
    # compute mean and standard deviation
    mean, sd = compute_stats(grade_list)
    # print out the mean and standard deviation in a nice format.
    print("****** Grade Statistics ******")
    print(f"The grades's mean is: {mean}")
    print(f"The population standard deviation of grades is: {round(sd, 3)}")
    print("****** END ******")


if __name__ == "__name__":
    n_students = 5
    print_stat(n_students)
