from django.db import models

# Create your models here.


# - Home홈
# - About센터소개
#     - Greeting인사말(page)
#     - Member멤버(list)
#     - Lab연구실소개(list)
#     - Project사업소개(page)
# - Research연구성과
#     - Github깃허브(link)
#     - LectureNote강연영상(imagelist,video)
#     - LectureVideo강연자료(imagelist)
#     - DemoResource시연자료(imagelist)
#     - Publication논문(textlist)
#     - Patent특허(textlist)
#     - Report기술보고서(textlist)
# - News&Info뉴스&정보
#     - Notice공지사항(textlist)
#     - News보도자료(imagelist)
#     - Gallery갤러리(imagelist)
#     - Community커뮤니티(board)
# - Contact오시는길(page)

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

# About
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

class Member(models.Model):
    nameko = models.CharField(max_length=100)
    nameen = models.CharField(max_length=100)
    positionko = models.CharField(max_length=100)
    positionen = models.CharField(max_length=100)
    departmentko = models.TextField()
    departmenten = models.TextField()
    educationko = models.TextField()
    educationen = models.TextField()
    careerko = models.TextField()
    careeren = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)
    # IMAGE UPLOAD
    testImage = models.ImageField(upload_to="member", default='noImage')

    def __str__(self):
        return self.nameen

class Lab(models.Model):
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

class Project(models.Model):
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

# Research
# Github admin으로 직접 넣기

class LectureNote(models.Model):
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

class LectureVideo(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    link = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class DemoResource(models.Model):
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

class Publication(models.Model):
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

class Patent(models.Model):
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

class Report(models.Model):
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

# News&Info
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
    writer = models.CharField(max_length=45)
    date = models.DateField()
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