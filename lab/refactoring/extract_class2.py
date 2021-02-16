# by Kami Bigdely
# Extract class


class Person:
    """Define fields and methods for a person."""

    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_yr = birth_year
        self.movies = movies
        self.email = email


# define data for people
first_names = ["elizabeth", "Jim"]
last_names = ["debicki", "Carrey"]
birth_year = [1990, 1962]
movies = [
    ["Tenet", "Vita & Virgina", "Guardians of the Galexy", "The Great Gatsby"],
    ["Ace Ventura", "The Mask", "Dubm and Dumber", "The Truman Show", "Yes Man"],
]
emails = ["deb@makeschool.com", "jim@makeschool.com"]

# instantiate the people
people = list()
for person_index in range(2):
    people.append(
        Person(
            first_names[person_index],
            last_names[person_index],
            birth_year[person_index],
            movies[person_index],
            emails[person_index],
        )
    )
# share the movies and send emails
def send_hiring_email(email):
    print("email sent to: ", email)


for person in people:
    if person.birth_yr > 1985:
        print(person.first_name, person.last_name)
        print("Movies Played: ", end="")
        for m in person.movies:
            print(m, end=", ")
        print()
        send_hiring_email(person.email)
