from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import date

class Researcher(models.Model):
    user = models.ForeignKey(User)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.user_name

class Review(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    date_started = models.DateField()
    query_string = models.CharField(max_length=30)
    pool_size = models.IntegerField(default=0)
    abstracts_judged = models.IntegerField(default=0)
    document_judged = models.IntegerField(default=0)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.title

class Query(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Paper(models.Model):
    review = models.ForeignKey(Review)
    title = models.CharField(max_length=30)
    authors = models.CharField(max_length=30)
    abstract = models.CharField(max_length=300)
    publish_date = models.DateField()
    paper_url = models.URLField()
    abstract_relevance = models.CharField(max_length=30)
    document_relevance = models.CharField(max_length=30)
    notes = models.CharField(max_length=30)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
