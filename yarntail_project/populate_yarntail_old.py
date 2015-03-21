from datetime import datetime
from pytz import UTC


__author__ = 'joshuamarsh'
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yarntail_project.settings')

import django

django.setup()

from yarntail.models import Comment, Pattern, Profile, User

def add_comment(profile, pattern, date, comment):
    com = Comment.objects.get_or_create(profile=profile, pattern=pattern, creation_date=date, comment_string=comment)[0]
    return com

def add_pattern(name, user, pattern, descr, date, comment, likes, views, favs, diff):
    pat = Pattern.objects.get_or_create(name=name, user=user,pattern_string=pattern, description=descr, creation_date=date,
                                      comment=comment, likes=likes, views=views, favorites=favs, difficulty=diff)
    return pat

def add_profile(user, com, pat, descr, likes, liked_p, liked_u, fav, fav_p, fav_u, views, date, num_p, dob):
    pro = Profile.objects.get_or_create(user=user, comment=com, pattern=pat, description=descr, likes=likes,
                                        liked_pattern=liked_p, liked_user=liked_u, favorites=fav,
                                        favorited_pattern=fav_p, favorited_user=fav_u, views=views,
                                        registration_date=date, number_of_patterns=num_p, date_of_birth=dob)
    return pro

def add_user(username, password, email):
    # may have issue assigning password
    use = User.objects.get_or_create(username=username, password=password, email=email)
    return use

def populate():

    gertrude = add_user('gertrude', 'password', "yarntailtest@yahoo.com")

    gertrudes_comment = add_comment(profile=None,
                                    pattern=None,
                                    date=datetime(12, 1, 23, 1, 59, 0, tzinfo=UTC),
                                    comment="This is a test comment for gertrude")

    gertrudes_pattern = add_pattern(name="gloves",
                                   user=User.objects.get(username='gertrude'),
                                   pattern="sspss",
                                   descr="This is the description for a pair of gloves.",
                                   date=datetime(11, 2, 22, 2, 58, 1, tzinfo=UTC),
                                   comment=gertrudes_comment,
                                   likes=5,
                                   views=6,
                                   favs=7,
                                   diff='M')

    gertrudes_comment.pattern = Pattern.objects.get(name='gloves')

    gertrudes_profile = add_profile(user=User.objects.get(username='gertrude'),
                                    com=gertrudes_comment,##
                                    pat=Pattern.objects.get(name='gloves'),
                                    descr="This is Gertrudes profile description",
                                    likes=3,
                                    liked_p=None,
                                    liked_u=None,
                                    fav=4,
                                    fav_p=None,
                                    fav_u=None,
                                    views=5,
                                    date=datetime(10, 3, 21, 3, 57, 2, tzinfo=UTC),
                                    num_p=1,
                                    dob=datetime(9, 4, 20, 4, 56, 3, tzinfo=UTC))
    gertrudes_comment.profile = Profile.objects.get(user=User.objects.get(username='gertrude'))



if __name__ == '__main__':
    print "Starting yarntail population script..."
    populate()
