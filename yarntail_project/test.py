from django.test import TestCase
from yarntail.models import UserProfile, Pattern, Comment
from django.contrib.auth.models import User
from django.db import models
import datetime

class UserProfileTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        UserProfile.objects.create(user=user, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))




    def test_Users_Have_Names(self):
        hulk = User.objects.get(username="Hulk")
        hulk_profile = UserProfile.objects.get(user=hulk)
        hulk_first_name = getattr(hulk_profile, 'first_name')
        hulk_last_name = getattr(hulk_profile, 'last_name')
        hulk_dob = getattr(hulk_profile, 'date_of_birth')
       # print "username:", hulk
       # print str(hulk_user) == 'Hulk'
        self.assertEqual(str(hulk_profile), 'Hulk')
        self.assertEqual(str(hulk_first_name), "Bruce")
        self.assertEqual(str(hulk_last_name), "Banner")
        self.assertEqual(str(hulk_dob), str(datetime.date(1962, 5, 1)))


