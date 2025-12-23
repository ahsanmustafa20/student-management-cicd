from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(
            name="Ali",
            roll_no="101",
            email="ali@test.com"
        )
        self.assertEqual(student.name, "Ali")
        self.assertEqual(student.roll_no, "101")
        self.assertEqual(student.email, "ali@test.com")
