from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import ast


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


    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})


class Pattern(models.Model):
    title = models.CharField(max_length=128,
                             unique=True)
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






