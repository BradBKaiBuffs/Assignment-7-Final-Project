from django.test import TestCase
from .models import Course

# unit test
class Test(TestCase):
    def test_basic_sum(self):
        assert 1+1 == 2

# model test
class TestCourseModel(TestCase):
    def setUp(self):
        self.p = Course(course_name="ENGL 1302")

    def test_create_course(self):
        self.assertIsNotNone(self.p, Course)

    def test_str_representation(self):
        self.assertEquals(str(self.p),"ENGL 1302")