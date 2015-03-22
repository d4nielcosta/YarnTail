import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yarntail_project.settings')

import django
django.setup()

from yarntail.models import *


def populate():

    add_admin()

    add_user(username="Hulk", password="marvel", email="hulkisgreen@gamma.com", first_name="Bruce", last_name="Banner", dob="1962-05-01")

    add_user(username="Wolverine", password="xmen", email="adamantium@skeleton.claws", first_name="James", last_name="Howlett", dob="1974-06-03")

    add_user(username='test', password='test', email='test@mailinator.com', first_name='Test', last_name='User', dob='1995-01-01')

    add_user(username='user1', password='password', email='awesome@captains_of_the_world.com', first_name='Captain', last_name='Awesome', dob='1990-12-12')

    add_pattern(title='Fingerless Gloves', description='Classy fingerless gloves. Perfect for a smartphone user', user='user1')

    add_pattern(title="Claw Cleaner", description="A useful tool for cleaning the blood of your enemies off your claws.", user="Wolverine")

    add_pattern(title="Incredible Shorts", description="A pair of shorts that won't break when you turn into a massive green "
                                                       "rage monster. HULK SMASH!", user="Hulk")

    add_pattern(title="testPattern", description="This is a pattern for test purposes.", user="test")

    add_comment(user='user1', pattern_slug='fingerless-gloves', comment='Tried this pattern and I loved it. I highly recommend it')

    add_comment(user="Hulk", pattern_slug="claw-cleaner", comment="Good to see you taking care of those claws, check out"
                                                                  "my Incredible Shorts pattern, may be useful in your fights. "
                                                                  "May no foe stand before you!")

    add_comment(user="Wolverine", pattern_slug="claw-cleaner", comment="Thanks Hulk, got to keep in top condition. I'll check it out now.")

    add_comment(user="Wolverine", pattern_slug="incredible-shorts", comment="These look really useful, going to start making them right away!")

    add_comment(user="Wolverine", pattern_slug="incredible-shorts", comment="Just test these bad boys out in a fight...no rips!"
                                                                            "Will use these from now on.")

    add_comment(user="Hulk", pattern_slug="incredible-shorts", comment="Glad you liked them Wolverine :)")

def add_user(username, password, first_name, last_name, email, dob):
    user = User.objects.create_user(username, email, password)
    user.save()

    prof = UserProfile.objects.get_or_create(user=user, first_name=first_name, last_name=last_name, date_of_birth=dob)
    return prof

def add_admin():
    user = User.objects.create_user('admin', '2087521d@student.gla.ac.uk', 'password')
    user.is_staff = True
    user.is_superuser = True
    user.save()

def add_pattern(title, description, user):
    pattern = Pattern.objects.create(title=title, description=description, user=User.objects.get(username=user))
    return pattern

def add_comment(user, pattern_slug, comment):
    comment = Comment.objects.create(user=User.objects.get(username=user), pattern=Pattern.objects.get(slug=pattern_slug), comment_string=comment)
    return comment

# Start execution here!
if __name__ == '__main__':
    print "Starting YarnTail population script..."
    populate()
