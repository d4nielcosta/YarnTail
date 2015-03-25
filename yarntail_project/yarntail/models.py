from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import ast

# class ListField(models.TextField):
# __metaclass__ = models.SubfieldBase
#     description = "Stores a python list"
#
#     def __init__(self, *args, **kwargs):
#         super(ListField, self).__init__(*args, **kwargs)
#
#     def to_python(self, value):
#         if not value:
#             value = []
#
#         if isinstance(value, list):
#             return value
#
#         return ast.literal_eval(value)
#
#     def get_prep_value(self, value):
#         if value is None:
#             return value
#
#         return unicode(value)
#
#     def value_to_string(self, obj):
#         value = self._get_val_from_obj(obj)
#         return self.get_db_prep_value(value)

# class ListModel(models.Model):
#     test_list = ListField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    date_of_birth = models.DateField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})


class Pattern(models.Model):
    title = models.CharField(max_length=128,
                             unique=True)  # in forms, prepend username before submitting "gertrude's rainbow gloves"
    user = models.ForeignKey(User, related_name='patterns')
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=3000)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    design = models.CharField(max_length=100000, default="empty pattern")
    difficulty = models.CharField(default="Easy", max_length=10)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pattern, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pattern', kwargs={'username_slug': self.user.user_profile.slug, 'pattern_slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    pattern = models.ForeignKey(Pattern, related_name='pattern')
    creation_date = models.DateTimeField(auto_now_add=True)
    comment_string = models.CharField(max_length=20000)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.creation_date)
        super(Comment, self).save(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.creation_date)






