# by Kami Bigdely
# Inline method.


class Person:

    LEGAL_DRINKING_AGE = 18

    def __init__(self, my_age):
        '''Instantiates a new Person object with an age (a float value).'''
        self.age = my_age


def enter_night_club(individual):
    """Displays if the person is allowed to enter the club.

    Args:
        individual: a Person instance.
    
    Returns: None
    """
    if individual.age > Person.LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")


if __name__ == "__main__": 
    person = Person(17.9)
    enter_night_club(person)
