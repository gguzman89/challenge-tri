from django.contrib import admin
from .models import Course, Level, Language, People

admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Language)
admin.site.register(People)