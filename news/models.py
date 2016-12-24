from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.TextField(max_length=100)

class News(models.Model):
    catagory = models.ManyToManyField(Catagory)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,blank=True)
    time = models.CharField(max_length=100)
    content = models.TextField()
    imgsrc = models.CharField(max_length=100,blank=True)

class Comment(models.Model):
    news = models.ManyToManyField(News)
    author = models.CharField(max_length=100)
    content = models.TextField()

