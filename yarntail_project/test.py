from django.test import TestCase
from yarntail.models import UserProfile, Pattern, Comment
from django.contrib.auth.models import User
from django.db import models
import datetime

class UserProfileTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        UserProfile.objects.create(user=user, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))

    def test_User_profile(self):
        hulk = User.objects.get(username="Hulk")
        hulk_profile = UserProfile.objects.get(user=hulk)
        self.assertEqual(str(hulk_profile), 'Hulk')

    def test_Users_Have_Names(self):
        hulk = User.objects.get(username="Hulk")
        hulk_profile = UserProfile.objects.get(user=hulk)
        hulk_first_name = getattr(hulk_profile, 'first_name')
        hulk_last_name = getattr(hulk_profile, 'last_name')
       # print "username:", hulk
       # print str(hulk_user) == 'Hulk'
        self.assertEqual(str(hulk_first_name), "Bruce")
        self.assertEqual(str(hulk_last_name), "Banner")

    def test_Users_DOB(self):
        hulk = User.objects.get(username="Hulk")
        hulk_profile = UserProfile.objects.get(user=hulk)
        hulk_dob = getattr(hulk_profile, 'date_of_birth')
        self.assertEqual(str(hulk_dob), str(datetime.date(1962, 5, 1)))

class PatternTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        UserProfile.objects.create(user=user, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))
        Pattern.objects.create(title="Incredible Shorts", user=user, difficulty="Easy",
                               description="A pair of shorts that won't break when you turn into a massive green "
                                           "rage monster. HULK SMASH!")

    def test_Pattern_title(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        self.assertEqual(str(pattern), "Incredible Shorts")

    def test_Pattern_USer(self):
        user = getattr(Pattern.objects.get(user=User.objects.get(username="Hulk")), 'user')
        self.assertEqual(str(user), "Hulk")

    def test_Pattern_difficulty(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        difficulty = getattr(pattern, "difficulty")
        self.assertEqual(str(difficulty), "Easy")
        self.assertNotEqual(str(difficulty), "easy")
        self.assertNotEqual(str(difficulty), "E")

    def test_Pattern_description(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        description = getattr(pattern, 'description')
        self.assertEqual(str(description), "A pair of shorts that won't break when you turn into a massive green "
                                           "rage monster. HULK SMASH!")
