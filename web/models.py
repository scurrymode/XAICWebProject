from django.db import models

# Create your models here.

#HOME, RESEARCH, NEWSAndINFO
class TopMenu(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)

class Greeting(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class About(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Member(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    careerko = models.TextField()
    careeren = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class LectureNote(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class LectureVideo(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    link = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class DemoResource(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Publication(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Patent(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Notice(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class News(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Gallery(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

class Community(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)