# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# Use 'extract method' refactoring technique to improve this code. If required, use
# 'replace temp variable with query' technique to make it easier to extract methods.


class Employer:    

    def __init__(self, name):
        self.name = name

    def send(self):
        print("Students' contact info were sent to", self.name + '.')


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
        return [
            s for s in self.students if s.get_gpa() > min_gpa
        ]

    def print_graduates(self, passed_students):
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')

    def share_with_employers(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passed_students = self.get_passed_students(2.5)
        # print student's name who graduated.
        self.print_graduates(passed_students)
        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()
        # Find the top 10% of them and send their contact to the top employers
        self.share_with_employers(passed_students)


if __name__ == "__main__":
    students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
                Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
    school  = School(students)
    school.process_graduation()
