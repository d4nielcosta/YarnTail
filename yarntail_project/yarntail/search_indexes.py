__author__ = 'joshuamarsh'
import datetime
from haystack import indexes
from models import Pattern, UserProfile


class PatternIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    creation_date = indexes.DateTimeField(model_attr='creation_date')
    content_auto = indexes.EdgeNgramField(model_attr='title')

    def get_model(self):
        return Pattern

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        #haystack tutorial uses return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
        return self.get_model().objects.all()


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content_auto = indexes.EdgeNgramField(model_attr='user')
    def get_model(self):
        return UserProfile

    def index_queryset(self, using=None):
        return self.get_model().objects.all()