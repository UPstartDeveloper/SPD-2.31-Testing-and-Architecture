# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/


def calculate_area(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max_value(li): 
    """Return the largest value from a list."""
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_max_value(li))

############################
def tokenize(sentence):  
    words = sentence[0:].split(' ')
    return words


print(tokenize('If you were a vegetable, you’d be a ‘cute-cumber.'))
