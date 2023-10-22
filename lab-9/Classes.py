class Student:
    """Represents a Student."""

    def __init__(self, last_name, first_name, sid, major):
        """Initialize a Student object"""
        self.last_name = last_name
        self.first_name = first_name
        self.sid = sid
        self.major = major
        self.course_work = {}

    def report(self):
        """Print a report on Student"""
        print("Student Information")
        print("\tName:\t{}, {}".format(self.last_name, self.first_name))
        print("\tSID:\t{}".format(self.sid))
        print("\tMajor:\t{}".format(self.major))

    def add_course(self, course, grade):
        """Add a course to the Students course_work dictionary"""
        self.course_work[course] = grade

    def __str__(self):
        """Return string representation of Student"""
        return (
            self.first_name
            + " "
            + self.last_name
            + " (SID: "
            + str(self.sid)
            + ")"
        )


class Course:
    """Represents a Course."""

    def __init__(self, title, semester, year):
        """Initialize a Course object"""
        self.title = title
        self.semester = semester
        self.year = year

    def __str__(self):
        """Return a string representation of Course"""
        return self.title + ": " + self.semester + ", " + str(self.year)
