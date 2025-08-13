from django.db import models

# Create your models here.
class Experience(models.Model):
    """ Medel to store experiences"""
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    jobtitle = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    description = models.TextField(max_length=2048, blank=True)

    def __str__(self) -> str:
        return f"{self.startdate}-{self.enddate}:{self.jobtitle}"


class SkillCategory(models.Model):
    """ Model to store technical skill categories"""
    name = models.CharField(max_length=100)


class Skills(models.Model):
    """ Model to store technical skills """
    category_id = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    skillname = models.CharField(max_length=100)


class Projects(models.Model):
    """ Model to store projects performed """
    name = models.CharField(max_length=200)
    skills = models.ManyToManyField(Skills)
    description = models.TextField(max_length=2048, blank=True)
    github_url = models.CharField(max_length=200, blank=True)
    live_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Contact(models.Model):
    """ Model to store contact details"""
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True)
