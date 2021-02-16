# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# Use 'extract method' refactoring technique to improve this code. If required, use
# 'replace temp variable with query' technique to make it easier to extract methods.


class Employer:
    def __init__(self, name):
        self.name = name

    def send(self):
        print("Students' contact info were sent to", self.name + ".")


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = dict()

    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]


class School:
    def __init__(self, students) -> None:
        self.students = students

    @Memoize
    def get_passed_students(self, min_gpa):
        return [s for s in self.students if s.get_gpa() > min_gpa]

    def print_graduates(self, passed_students):
        print("*** Student who graduated *** ")
        for s in passed_students:
            print(s.name)
        print("****************************")

    def share_with_employers(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [
            Employer("Microsoft"),
            Employer("Free Software Foundation"),
            Employer("Google"),
        ]
        for e in top_employers:
            e.send(top_10_percent)


students = [
    Student(2.1, "Pinocchio"),
    Student(2.3, "goku"),
    Student(2.7, "toro"),
    Student(3.9, "naruto"),
    Student(3.2, "kami"),
    Student(3, "guts"),
]
school = School(students)
school.process_graduation()
