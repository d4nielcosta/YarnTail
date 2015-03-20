from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


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


class Pattern(models.Model):
    title = models.CharField(max_length=128,
                             unique=True)  # in forms, prepend username before submitting "gertrude's rainbow gloves"
    user = models.ForeignKey(User, related_name='patterns')
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=3000)
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pattern, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

#Need to add comment once everything else is functional

    # #name = models.CharField(max_length=128,
    #                         unique=True)  # in forms, prepend username before submitting "gertrude's rainbow gloves"
    # #user = models.ForeignKey(User, related_name='patterns')
    # # should pattern_string be unique? would it take to long to check if its unique?????
    # pattern_string = models.CharField(max_length=20000)
    # #description = models.CharField(max_length=3000)
    # #creation_date = models.DateTimeField()
    # comment = models.ForeignKey('Comment', related_name='commented_pattern')
    # likes = models.IntegerField()
    # views = models.IntegerField()
    # favorites = models.IntegerField()
    # # Difficulty Choices
    # HARD = 'H'
    # MEDIUM = 'M'
    # EASY = 'E'
    # DIFFICULTY_CHOICES = (
    #     (HARD, 'Hard'),
    #     (MEDIUM, 'Medium'),
    #     (EASY, 'Easy'),
    # )
    # # difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default=EASY)
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Pattern, self).save(*args, **kwargs)
    #
    # def __unicode__(self):
    #     return self.name