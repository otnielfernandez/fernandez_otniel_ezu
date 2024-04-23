from django.contrib.auth import get_user_model
from .models import Period, Year, Semester, Course, Instructor, Student, Section, Registration
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.http import Http404
from .models import Semester




#####################################Update and Delete Tests########################################################################



class StudentUpdateDeleteTestCase(TestCase):
    def setUp(self):
        # Create a sample student object
        self.student = Student.objects.create(first_name='John', last_name='Doe')

    def test_update_student_name(self):
        new_first_name = 'Jane'
        new_last_name = 'Doe'
        # Make a POST request
        response = self.client.post(reverse('courseinfo_student_update_urlpattern', kwargs={'pk': self.student.pk}), {'first_name': new_first_name, 'last_name': new_last_name})
        # Check if the update was successful
        self.assertEqual(response.status_code, 302)  # redirect
        self.student.refresh_from_db()  # refresh
        self.assertEqual(self.student.first_name, new_first_name)
        self.assertEqual(self.student.last_name, new_last_name)
    def test_delete_student(self):
        # delete student
        response = self.client.post(reverse('courseinfo_student_delete_urlpattern', kwargs={'pk': self.student.pk}))
        # Check if delete was successful
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after delete
        self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())  # no longer exists in the db




#############################LINKED PAGES TESTS#######################################################




# class HomePageNavigationTestCase(TestCase):
#     def test_navigation_to_other_pages(self):
#         response_homepage = self.client.get('/section/')
#         self.assertEqual(response_homepage.status_code, 200)
#         links = {
#             'course': '/course/',
#             'instructor': '/instructor/',
#             'student': '/student/',
#             'semester': '/semester/',
#             'registration': '/registration/',
#         }
#         # iterate through links from homepage
#         for link_name, link_href in links.items():
#             with self.subTest(link_name=link_name):
#                 response_other_page = self.client.get(link_href)
#                 self.assertEqual(response_other_page.status_code, 200)


#
# testing whether each detailed link is valid
# class SemesterDetailTest(TestCase):
#
#     def test_valid_semester_and_pk(self):
#         semester = Semester.objects.create(name="Fall 2023")
#         client = Client()
#         response = client.get(f'/{semester.pk}/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_invalid_semester_and_pk(self):
#         invalid_pk = 1000
#         client = Client()
#         with self.assertRaises(Http404):
#             client.get(f'/{invalid_pk}/')
#
#
#





# class ModelTestCase(TestCase):
#     def setUp(self):
#         Create a test user
        # self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        #
        # Create test instances of each model
        # self.period = Period.objects.create(period_sequence=1, period_name='Spring')
        # self.year = Year.objects.create(year=2024)
        # self.semester = Semester.objects.create(year=self.year, period=self.period)
        # self.course = Course.objects.create(course_number='IS101', course_name='Introduction to IS')
        # self.instructor = Instructor.objects.create(first_name='John', last_name='Doe')
        # self.student = Student.objects.create(first_name='Alice', last_name='Smith')
        # self.section = Section.objects.create(section_name='001', semester=self.semester, course=self.course, instructor=self.instructor)
        # self.registration = Registration.objects.create(student=self.student, section=self.section)
    # next steps
    # chapter 6 of vincent
    # check plumbing of links (name -> section)







    # def test_period_str_representation(self):
    #     self.assertEqual(str(self.period), 'Spring')
    #
    # def test_year_str_representation(self):
    #     self.assertEqual(str(self.year), '2024')
    #
    # def test_semester_str_representation(self):
    #     expected_str = '2024 - Spring'
    #     self.assertEqual(str(self.semester), expected_str)
    #
    # def test_course_str_representation(self):
    #     expected_str = 'IS101 - Introduction to IS'
    #     self.assertEqual(str(self.course), expected_str)
    #
    # def test_instructor_str_representation(self):
    #     expected_str = 'Doe, John'
    #     self.assertEqual(str(self.instructor), expected_str)
    #
    # def test_student_str_representation(self):
    #     expected_str = 'Smith, Alice'
    #     self.assertEqual(str(self.student), expected_str)
    #
    # def test_section_str_representation(self):
    #     expected_str = 'IS101 - 001 (2024 - Spring)'
    #     self.assertEqual(str(self.section), expected_str)
    #
    # def test_registration_str_representation(self):
    #     expected_str = 'IS101 - 001 (2024 - Spring) / Smith, Alice'
    #     self.assertEqual(str(self.registration), expected_str)
    #
    # def test_unique_semester(self):
    #     Attempt to create a duplicate semester
        # with self.assertRaises(Exception):
        #     Semester.objects.create(year=self.year, period=self.period)
    #
    # def test_unique_course(self):
    #     Attempt to create a duplicate course
        # with self.assertRaises(Exception):
        #     Course.objects.create(course_number='IS101', course_name='Introduction to IS')
    #
    # def test_unique_instructor(self):
    #     Attempt to create a duplicate instructor
        # with self.assertRaises(Exception):
        #     Instructor.objects.create(user=self.user, first_name='John', last_name='Doe')
    #
    # def test_unique_student(self):
    #     Attempt to create a duplicate student
        # with self.assertRaises(Exception):
        #     Student.objects.create(user=self.user, first_name='Alice', last_name='Smith')
    #
    # def test_unique_section(self):
    #     Attempt to create a duplicate section
        # with self.assertRaises(Exception):
        #     Section.objects.create(section_name='001', semester=self.semester, course=self.course, instructor=self.instructor)
    #
    # def test_unique_registration(self):
    #     Attempt to create a duplicate registration
        # with self.assertRaises(Exception):
        #     Registration.objects.create(student=self.student, section=self.section)
