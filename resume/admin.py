
from django.contrib import admin
from .models import Experience, Projects, Contact, SkillCategory, Skills

# Register your models here.
admin.site.register(Experience)
admin.site.register(Projects)
admin.site.register(SkillCategory)
admin.site.register(Skills)