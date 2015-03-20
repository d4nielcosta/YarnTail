from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Comment(models.Model):
    profile = models.ForeignKey('Profile', related_name='comments', null=True)
    pattern = models.ForeignKey('Pattern', related_name='comments', null=True)
    creation_date = models.DateTimeField()
    # comment_string has roughly 350 words
    comment_string = models.CharField(max_length=2100)

    def save(self, *args, **kwargs):
        # this may not work
        if self.pattern:
            self.slug = slugify(self.pattern.name, self.creation_date)
        if self.profile:
            self.slug = slugify(self.profile.username, self.creation_date)
        super(Comment, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug


class Pattern(models.Model):
    name = models.CharField(max_length=128,
                            unique=True)  # in forms, prepend username before submitting "gertrude's rainbow gloves"
    user = models.ForeignKey(User, related_name='patterns')
    # should pattern_string be unique? would it take to long to check if its unique?????
    pattern_string = models.CharField(max_length=20000)
    description = models.CharField(max_length=3000)
    creation_date = models.DateTimeField()
    comment = models.ForeignKey('Comment', related_name='commented_pattern')
    likes = models.IntegerField()
    views = models.IntegerField()
    favorites = models.IntegerField()
    # Difficulty Choices
    HARD = 'H'
    MEDIUM = 'M'
    EASY = 'E'
    DIFFICULTY_CHOICES = (
        (HARD, 'Hard'),
        (MEDIUM, 'Medium'),
        (EASY, 'Easy'),
    )
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default=EASY)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Pattern, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User)
    comment = models.ForeignKey('Comment', related_name='commented_profile')
    pattern = models.ForeignKey('Pattern')
    # description has roughly 500 words
    description = models.CharField(max_length=3000)
    likes = models.IntegerField()
    liked_pattern = models.ForeignKey('Pattern', related_name='users_that_like_this', null=True)
    liked_user = models.ForeignKey(User, related_name='users_that_like_this', null=True)# this should be changed to 'liked_profile'
    favorites = models.IntegerField()
    favorited_pattern = models.ForeignKey('Pattern', related_name='users_that_favorite_this', null=True)
    favorited_user = models.ForeignKey(User, related_name='users_that_favorite_this', null=True)
    views = models.IntegerField()
    registration_date = models.DateTimeField()
    number_of_patterns = models.IntegerField()
    date_of_birth = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug



