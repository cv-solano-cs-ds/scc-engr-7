"""
Contains `Course` and `Student` classes.
"""


# To allow type hinting for `Student` type parameters inside `Student` class.
from __future__ import annotations


class Course:
    """Represents a Course."""

    def __init__(self, title: str, semester: str, year: str):
        """
        Initialize a Course object
        """

        self.title = title
        self.semester = semester
        self.year = year
        self._students_enrolled = 0

    def increment_enrollment(self):
        """
        Increments the number of students enrolled in the course.
        """
        self._students_enrolled += 1

    def student_enrollment(self):
        """
        Returns the number of students in the course.
        """
        return self._students_enrolled

    def __str__(self):
        """
        Return a string representation of Course
        """
        return self.title + ": " + self.semester + ", " + str(self.year)


class Student:
    """Represents a Student."""

    def __init__(self, last_name: str, first_name: str, sid: int, major: str):
        """
        Initialize a Student object
        """

        self.last_name = last_name
        self.first_name = first_name
        self.sid = sid
        self.major = major
        self.course_work = {}

    def report(self) -> None:
        """
        Print a report on Student
        """

        print("Student Information")
        print("\tName:\t{}, {}".format(self.last_name, self.first_name))
        print("\tSID:\t{}".format(self.sid))
        print("\tMajor:\t{}".format(self.major))

    def add_course(self, course: Course, grade: str) -> None:
        """
        Add a course to the Students course_work dictionary
        """
        self.course_work[course] = grade
        course.increment_enrollment()

    def __str__(self) -> None:
        """
        Return string representation of Student
        """
        return (
            self.first_name
            + " "
            + self.last_name
            + " (SID: "
            + str(self.sid)
            + ")"
        )

    def __eq__(self, other: Student) -> bool:
        return self.sid == other.sid

    def __lt__(self, other: Student) -> bool:
        return self.sid < other.sid

    def __gt__(self, other: Student) -> bool:
        return self.sid > other.sid
