from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from main.models import Subject


class SigninTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@gmail.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model()

    def test_post_response(self):
        response = self.client.post('/register/', {
            "username": 'test',
            "email": "test@gmail.com",
            "password1": "12test12",
            "password2": "12test12",
            "user_type": "student"
        })
        self.assertEqual(response.status_code, 200)


# class SubjectTestCase(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model()
#         self.subject = Subject.objects.create(name='Biology', subject_id='test', standard='2nd Class')
#
#     def test_is_instance(self):
#         self.assertIsInstance(self.subject, Subject)
#
#     def test_subject_name(self):
#         self.assertEqual(self.subject.name, "Biology")

# class SignInViewTest(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test',
#                                                          password='12test12',
#                                                          email='test@gmail.com')
#
#     def tearDown(self):
#         self.user.delete()
#
#     def test_correct(self):
#         response = self.client.post('/user_login/', {'username': 'test', 'password': '12test12'})
#         self.assertTrue(response.data['authenticated'])
#
#     def test_wrong_username(self):
#         response = self.client.post('/user_login/', {'username': 'wrong', 'password': '12test12'})
#         self.assertFalse(response.data['authenticated'])
#
#     def test_wrong_password(self):
#         response = self.client.post('/user_login/', {'username': 'test', 'password': 'wrong'})
#         self.assertFalse(response.data['authenticated'])


