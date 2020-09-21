from django.contrib import admin
from django.db import models
from . models import Introduction, Project, Education, Skill, Language, Tools, Connect

# Register your models here.


# allows customizable apps
class ProjectAdmin(admin.ModelAdmin):

    # can have different dividers
    fieldsets = [
        ("Content", {'fields' : ["intro_content", "second_intro_content"]})
    ]

# allows customizable apps
class IntrotAdmin(admin.ModelAdmin):

    # can have different dividers
    fieldsets = [
        ("Title", {'fields' : ["project_title"]}),
        ("Summary", {'fields' : ["project_summary"]}),
        ("Technologies", {'fields' : ["project_technologies"]}),
        ("Git URL", {'fields' : ["project_git_url"]})
    ]

class EduAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name of Institute",   {'fields' : ["name_of_place"]}),
        ("Level of Education",  {'fields' : ["level_of_ed"]}),
        ("Dates",               {'fields' : ["dates_of_place"]}),
        ("Location",            {'fields' : ["location_of_place"]}),
        ("Grade / Gpa",         {'fields' : ["grade_received"]})
    ]


Abilities = [Skill, Language, Tools]
# registering without a class means taking variables names from the model class
admin.site.register(Abilities)
admin.site.register(Connect)
# 2. register models so you can see it on admin page
admin.site.register(Education, EduAdmin)
admin.site.register(Introduction, ProjectAdmin) 
admin.site.register(Project, IntrotAdmin) 