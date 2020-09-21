from django.db import models

# Create your models here.
# model will store my short introduction
class Introduction(models.Model):

    intro_content = models.TextField(default="Some string")
    second_intro_content = models.TextField(default="Some string")
    # overwriting string method
    def __str__(self):
        return self.intro_content


class Education(models.Model):
    # Ramapo College of New Jersey
    name_of_place = models.TextField(default="Some string")
    # gpa / grade (3.8/4.0)
    grade_received = models.TextField(default="Some string")
    # Bachelor of science in computer Science
    level_of_ed = models.TextField(default="Some string")
    # 2018 september - 2021 December
    dates_of_place = models.TextField(default="Some string")
    # New Jersey, USA
    location_of_place = models.TextField(default="Some string")

    # overwriting string method
    def __str__(self):
        return self.name_of_place


class Skill(models.Model):
    skill_name = models.TextField(default="Some string")
    skill_rating = models.TextField(default="Some string")

    # overwriting string method
    def __str__(self):
        return self.skill_name


class Language(models.Model):
    language_name = models.TextField(default="Some string")
    language_rating = models.TextField(default="Some string")

    # overwriting string method
    def __str__(self):
        return self.language_name

class Tools(models.Model):
    tool_name = models.TextField(default="Some string")
    tool_rating = models.TextField(default="Some string")

    # overwriting string method
    def __str__(self):
        return self.tool_name


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_summary = models.TextField(default='Some string')
    project_technologies = models.TextField(default='Some string')
    project_git_url = models.TextField(default='String')

    # overwriting string method
    def __str__(self):
        return self.project_title

class Connect(models.Model):

    social_network = models.TextField(default='Some string')
    my_url = models.TextField(default='Some string')
    

    # overwriting string method
    def __str__(self):
        return self.social_network