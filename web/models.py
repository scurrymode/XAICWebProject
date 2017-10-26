from django.db import models

# Create your models here.

#HOME, RESEARCH, NEWSAndINFO
class TopMenu(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)

    def __str__(self):
        return self.titleen


class SubMenu(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

    def __str__(self):
        return self.titleen

class Greeting(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class About(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Member(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    careerko = models.TextField()
    careeren = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class LectureNote(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class LectureVideo(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    link = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class DemoResource(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Publication(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Patent(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Notice(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class News(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Gallery(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Community(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen