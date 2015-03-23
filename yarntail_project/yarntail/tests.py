from django.test import TestCase, RequestFactory
from yarntail.models import UserProfile, Pattern, Comment
from django.contrib.auth.models import User
from django.test import Client
from yarntail.views import search_results
import datetime

class SearchPatternTestCase(TestCase):

   # print "test search"
    def setUp(self):
        # need access to the request factory.
        self.factory = RequestFactory()

        self.user = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        self.userProfile = UserProfile.objects.create(user=self.user, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))
        self.pattern1 = Pattern.objects.create(title="Incredible Shorts", user=self.user, difficulty="Easy", likes=5, views=10,
                               description="A pair of shorts that won't break when you turn into a massive green "
                                           "rage monster. HULK SMASH!")

        self.user2 = User.objects.create_user("Abomination", "abonimationrox@abom.com", "abomIsGr8")
        self.userProfile2 = UserProfile.objects.create(user=self.user2, first_name="Emil", last_name="Blonsky", date_of_birth=datetime.date(1964, 4, 1))
        self.pattern2 = Pattern.objects.create(title="HulkBuster Sweater", user =self.user2, difficulty="Hard", likes=6, views=15,
                                          description="A sweater sporting the HulkBuster's iron face.")

        # needs a Client.
        self.client = Client()

    def test_Search_Patterns(self):
        # Issue a GET request.
        request = self.factory.get('/search_results/')

        # simulate a logged in user.
        request.user = self.user2

        response = search_results(request, query="Incredible Shorts")
        # print response

        self.assertIn("Incredible Shorts", response.content)

        # new logged in user.
        request.user = self.user

        # test to see if user can search on patterns correctly.
        response = search_results(request, query="HulkBuster Sweater")

        self.assertIn("HulkBuster Sweater", response.content)

        response = search_results(request, query="Incredible Shorts")

        self.assertIn("Incredible Shorts", response.content)

class UserProfileTestCase(TestCase):
    # Creates a user and UserProfile object and tests the required fields exist correctly.

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
    # Creates a user and UserProfile and associates a pattern with the profile, tests pattern attributes.

    def setUp(self):
        user = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        UserProfile.objects.create(user=user, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))
        Pattern.objects.create(title="Incredible Shorts", user=user, difficulty="Easy", likes=5, views=10,
                               description="A pair of shorts that won't break when you turn into a massive green "
                                           "rage monster. HULK SMASH!")

    def test_Pattern_title(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        self.assertEqual(str(pattern), "Incredible Shorts")

    def test_Pattern_Likes(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        likes = getattr(pattern, 'likes')
        self.assertEqual(str(likes), '5')

    def test_Pattern_Views(self):
        pattern = Pattern.objects.get(title="Incredible Shorts")
        views = getattr(pattern, 'views')
        self.assertEqual(str(views), '10')

    def test_Pattern_User(self):
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

class CommentTestCase(TestCase):
    # Creates two users, two UserProfiles, a pattern associated with one profile and a comment by one user about
    # the pattern. Tests that the comment attributes are correct.

    def setUp(self):
        user1 = User.objects.create_user("Hulk", "gammaradiationisfun@greenman.com", "password")
        UserProfile.objects.create(user=user1, first_name="Bruce", last_name="Banner", date_of_birth=datetime.date(1962, 5, 1))
        pattern = Pattern.objects.create(title="Incredible Shorts", user=user1, difficulty="Easy",
                               description="A pair of shorts that won't break when you turn into a massive green "
                                           "rage monster. HULK SMASH!")

        user2 = User.objects.create_user("Abomination", "abonimationrox@abom.com", "abomIsGr8")
        UserProfile.objects.create(user=user2, first_name="Emil", last_name="Blonsky", date_of_birth=datetime.date(1964, 4, 1))
        Comment.objects.create(user=user2, pattern=pattern,
                               comment_string="Shorts ripped on abomination...Abomination stronger than Hulk!")


    def test_Comment_User(self):
        user = getattr(Comment.objects.get(user=User.objects.get(username="Abomination")), 'user')
        self.assertEqual(str(user), "Abomination")

    def test_Comment_Pattern(self):
        comment = Comment.objects.get(user=User.objects.get(username="Abomination"))
        pattern = getattr(comment, 'pattern')
        self.assertEqual(str(pattern), "Incredible Shorts")

    def test_Comment_String(self):
        comment = Comment.objects.get(user=User.objects.get(username="Abomination"))
        data = getattr(comment, 'comment_string')
        self.assertEqual(str(data), "Shorts ripped on abomination...Abomination stronger than Hulk!")