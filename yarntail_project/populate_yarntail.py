import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yarntail_project.settings')

import django
django.setup()

from yarntail.models import *


def populate():

    add_admin()

    add_user(username='test', password='test', email='test@mailinator.com', first_name='Test', last_name='User', dob='1995-01-01')

    add_user(username='user1', password='password', email='awesome@captains_of_the_world.com', first_name='Captain', last_name='Awesome', dob='1990-12-12')

    add_pattern(title='Fingerless Gloves', description='Classy fingerless gloves. Perfect for a smartphone user', user='user1')

    add_comment(user='user1', pattern_slug='fingerless-gloves', comment='Tried this pattern and I loved it. I highly recommend it')

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
